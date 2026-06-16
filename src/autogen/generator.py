from __future__ import annotations

import os
from typing import Any, Dict

from crewai import project
from openai import project
from jinja2 import Environment, FileSystemLoader

from ..core.models import CrewProject, ProcessType


def _create_jinja_env() -> Environment:
    template_dir = os.path.join(
        os.path.dirname(__file__),
        "templates"
    )

    return Environment(
        loader=FileSystemLoader(template_dir),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )


def _build_team_context(
    project: CrewProject,
) -> Dict[str, Any]:

    model_name = "gpt-4o-mini"

    if (
        project.language_models
        and project.language_models[0].model_name
    ):
        extracted_model = (
            project.language_models[0]
            .model_name
            .strip()
        )

        if extracted_model:
            model_name = extracted_model
    """
    team_type = (
        "SelectorGroupChat"
        if project.process == ProcessType.HIERARCHICAL
        else "RoundRobinGroupChat"
    )
    """
    team_type = "RoundRobinGroupChat"

    ordered_tasks = project.tasks

    if project.workflow_steps:

        task_map = {

            t.var_name: t

            for t in project.tasks

        }

        ordered_tasks = []

        for step in sorted(

            project.workflow_steps,

            key=lambda s: s.step_order

        ):

            task = task_map.get(

                step.task_var_name

            )

            if task:

                ordered_tasks.append(task)

    if not ordered_tasks:

        default_prompt = """

Have a conversation according to your roles.

Stay in character.

End naturally when appropriate.

"""

    else:

        default_prompt = None
    
    tool_defs = []

    for tool in project.tools:
        tool_defs.append(
            {
                "var_name": tool.var_name,
                "class_name": tool.class_name,
                "description": tool.description,
            }
        )

    return {
    "project": project,
    "model_name": model_name,
    "team_type": team_type,
    "ordered_tasks": ordered_tasks,
    "default_prompt": default_prompt,
    "tool_defs": tool_defs,
}


def _build_main_context(
    project: CrewProject,
) -> Dict[str, Any]:

    return {
        "crew_name": project.crew_name,
        "input_variables": project.input_variables,
    }

def _build_tool_context(project: CrewProject):

    tool_defs = []

    for tool in project.tools:

        tool_defs.append(
            {
                "var_name": tool.var_name,
                "class_name": tool.class_name,
                "description": tool.description,
                "configs": tool.configs,
            }
        )

    return tool_defs

def generate_project(
    project: CrewProject,
    output_dir: str,
) -> str:

    os.makedirs(
        output_dir,
        exist_ok=True,
    )

    env = _create_jinja_env()

    team_template = env.get_template(
        "team.py.j2"
    )

    team_ctx = _build_team_context(
        project
    )

    with open(
        os.path.join(output_dir, "team.py"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(
            team_template.render(
                **team_ctx
            )
        )

    main_template = env.get_template(
        "main.py.j2"
    )

    main_ctx = _build_main_context(
        project
    )

    with open(
        os.path.join(output_dir, "main.py"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(
            main_template.render(
                **main_ctx
            )
        )

    requirements = """
autogen-agentchat>=0.4.0
autogen-ext>=0.4.0
openai
python-dotenv
"""

    with open(
        os.path.join(
            output_dir,
            "requirements.txt",
        ),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(
            requirements.strip()
        )

    return output_dir