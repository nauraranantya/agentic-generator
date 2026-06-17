from __future__ import annotations

from typing import Dict, List, Optional

from ..core.models import AgenticProject, AutoGenProject, TaskModel


def _resolve_model_name(project: AgenticProject) -> str:
    if project.language_models and project.language_models[0].model_name:
        return project.language_models[0].model_name.strip()
    return "gpt-4o-mini"


def _build_ordered_tasks(project: AgenticProject) -> List[TaskModel]:
    if not project.workflows:
        return list(project.tasks)

    task_by_iri: Dict[str, TaskModel] = {t.iri: t for t in project.tasks}

    seen: set = set()
    ordered: List[TaskModel] = []
    for workflow in project.workflows:
        for step in sorted(workflow.steps, key=lambda s: s.step_order):
            task = task_by_iri.get(step.task_iri)
            if task and task.var_name not in seen:
                seen.add(task.var_name)
                ordered.append(task)

    remaining = [t for t in project.tasks if t.var_name not in seen]
    ordered.extend(remaining)

    return ordered or list(project.tasks)


def adapt(project: AgenticProject) -> AutoGenProject:
    """Map AgenticProject into AutoGenProject for the AutoGen generator."""
    return AutoGenProject(
        name=project.name,
        model_name=_resolve_model_name(project),
        agents=project.agents,
        tasks=list(project.tasks),
        tools=project.tools,
        ordered_tasks=_build_ordered_tasks(project),
        input_variables=project.input_variables,
        env_vars=project.env_vars,
    )
