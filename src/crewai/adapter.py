from __future__ import annotations

from typing import Dict, List

from ..core.models import AgenticProject, CrewProject, ProcessType, WorkflowStepModel


def _infer_process(project: AgenticProject) -> ProcessType:
    process_value = project.system_configs.get("process", "").strip().lower()
    if "hierarchical" in process_value:
        return ProcessType.HIERARCHICAL

    for workflow in project.workflows:
        if workflow.workflow_type.value == "hierarchical":
            return ProcessType.HIERARCHICAL
    return ProcessType.SEQUENTIAL


def _flatten_workflow_steps(project: AgenticProject) -> List[WorkflowStepModel]:
    if not project.workflows:
        return []

    by_iri: Dict[str, WorkflowStepModel] = {}
    for workflow in project.workflows:
        for step in workflow.steps:
            key = step.iri or f"{workflow.iri}:{step.step_order}:{step.task_iri}"
            if key not in by_iri:
                by_iri[key] = step

    return sorted(by_iri.values(), key=lambda step: step.step_order)


def adapt(project: AgenticProject) -> CrewProject:
    """Adapt framework-agnostic AgenticProject into CrewProject."""
    tools_by_iri = {tool.iri: tool for tool in project.tools}
    agents_by_iri = {agent.iri: agent for agent in project.agents}

    for agent in project.agents:
        if not agent.backstory and agent.system_prompt:
            agent.backstory = agent.system_prompt
        if not agent.system_prompt and agent.backstory:
            agent.system_prompt = agent.backstory

        if not agent.tool_var_names and agent.tool_iris:
            for tool_iri in agent.tool_iris:
                tool = tools_by_iri.get(tool_iri)
                if tool and tool.var_name not in agent.tool_var_names:
                    agent.tool_var_names.append(tool.var_name)

        if not agent.language_model and agent.llm:
            agent.language_model = agent.llm
        if not agent.llm and agent.language_model:
            agent.llm = agent.language_model

        if agent.allow_delegation is None and "allow_delegation" in agent.configs:
            value = agent.configs["allow_delegation"].strip().lower()
            agent.allow_delegation = value in ("true", "1", "yes")
        if agent.verbose is None and "verbose" in agent.configs:
            value = agent.configs["verbose"].strip().lower()
            agent.verbose = value not in ("false", "0", "no", "none")

    for task in project.tasks:
        if not task.description and task.prompt_instruction:
            task.description = task.prompt_instruction
        if not task.expected_output and task.prompt_output_indicator:
            task.expected_output = task.prompt_output_indicator
        if not task.expected_output:
            task.expected_output = f"Completed: {task.var_name}"

        if not task.agent_var_name and task.agent_iri and task.agent_iri in agents_by_iri:
            task.agent_var_name = agents_by_iri[task.agent_iri].var_name

    workflow_steps = _flatten_workflow_steps(project)

    return CrewProject(
        crew_name=project.name,
        crew_var_name=project.var_name,
        description=project.description,
        process=_infer_process(project),
        agents=project.agents,
        tasks=project.tasks,
        tools=project.tools,
        workflow_steps=workflow_steps,
        input_variables=project.input_variables,
        language_models=project.language_models,
        env_vars=project.env_vars,
    )
