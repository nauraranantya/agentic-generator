from __future__ import annotations

from typing import Dict, List, Set

from ..core.models import (
    AgenticProject,
)
from .models import LangGraphAgentModel, LangGraphEdgeModel, LangGraphNodeModel, LangGraphProject, LangGraphToolModel


def _map_tools(project: AgenticProject) -> List[LangGraphToolModel]:
    mapped: List[LangGraphToolModel] = []
    for tool in project.tools:
        mapped.append(
            LangGraphToolModel(
                iri=tool.iri,
                var_name=tool.var_name,
                title=tool.label or tool.class_name or tool.var_name,
                description=tool.description or "A tool",
            )
        )
    return mapped


def _map_agents(project: AgenticProject) -> List[LangGraphAgentModel]:
    mapped: List[LangGraphAgentModel] = []
    for agent in project.agents:
        lm = agent.language_model or agent.llm
        model_name = lm.model_name if lm and lm.model_name else "gpt-4o-mini"
        prompt = agent.system_prompt or agent.backstory or "You are a helpful assistant."
        mapped.append(
            LangGraphAgentModel(
                iri=agent.iri,
                var_name=agent.var_name,
                role=agent.role or "agent",
                prompt=prompt,
                model_name=model_name,
                tools_refs=agent.tool_iris,
            )
        )
    return mapped


def _map_nodes_edges(project: AgenticProject) -> tuple[List[LangGraphNodeModel], List[LangGraphEdgeModel]]:
    step_by_iri: Dict[str, LangGraphNodeModel] = {}
    edges: List[LangGraphEdgeModel] = []

    for workflow in project.workflows:
        for step in workflow.steps:
            if not step.iri:
                continue
            step_by_iri[step.iri] = LangGraphNodeModel(
                iri=step.iri,
                name=step.var_name or step.task_var_name or "step",
                agent_ref=step.agent_iri or None,
                is_start=step.step_type == "StartStep",
                is_end=step.step_type == "EndStep",
            )
            for target in step.next_step_iris:
                edges.append(LangGraphEdgeModel(source=step.iri, target=target))

    if not step_by_iri:
        for idx, task in enumerate(project.tasks):
            step_iri = f"task-step:{task.iri}"
            step_by_iri[step_iri] = LangGraphNodeModel(
                iri=step_iri,
                name=task.var_name,
                agent_ref=task.agent_iri or None,
                is_start=idx == 0,
                is_end=idx == len(project.tasks) - 1,
            )
            if idx > 0:
                prev_iri = f"task-step:{project.tasks[idx - 1].iri}"
                edges.append(LangGraphEdgeModel(source=prev_iri, target=step_iri))

    has_outgoing = {edge.source for edge in edges}
    for node in step_by_iri.values():
        if node.iri not in has_outgoing and len(step_by_iri) > 0:
            node.is_end = True

    return list(step_by_iri.values()), edges


def adapt(project: AgenticProject) -> LangGraphProject:
    """Adapt framework-agnostic AgenticProject into LangGraphProject."""
    tools = _map_tools(project)
    agents = _map_agents(project)
    nodes, edges = _map_nodes_edges(project)

    # Mark tasks that involve human agents
    human_participated: Set[str] = set()
    for ha in project.human_agents:
        for task_iri in ha.participated_task_iris:
            human_participated.add(task_iri)

    for task in project.tasks:
        if task.iri in human_participated:
            task.human_input = True

    return LangGraphProject(
        name=project.name or "LangGraph Project",
        tools=tools,
        agents=agents,
        nodes=nodes,
        edges=edges,
        input_variables=project.input_variables,
        tasks=list(project.tasks),
        human_agents=project.human_agents,
        goals=project.goals,
        objectives=project.objectives,
        capabilities=project.capabilities,
        environments=project.environments,
        resources=project.resources,
        constraints=project.constraints,
    )
