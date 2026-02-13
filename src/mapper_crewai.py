"""
CrewAI Code Generator from AgentO KG

This module compiles a parsed AgentO knowledge graph
into executable CrewAI Python source code.

Public API:
- generate_crewai_code(parsed: dict) -> str
"""

from typing import Dict, Any
import re
import textwrap


# --------------------------------------------------
# Helpers
# --------------------------------------------------

def safe_name(iri: str) -> str:
    """
    Convert an IRI into a valid Python identifier.
    """
    if not iri:
        return "unnamed"
    name = iri.split("/")[-1].split("#")[-1]
    name = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    if not name:
        name = "unnamed"
    if name[0].isdigit():
        name = f"_{name}"
    return name


def infer_output_kind(task: Dict[str, Any]) -> str:
    """
    Infer output format from produced resources and prompt hints.
    """
    for r in task.get("produced_resources", []):
        r_lower = r.lower()
        if r_lower.endswith(".py"):
            return "python_code"
        if r_lower.endswith(".md"):
            return "markdown"
    return "plain_text"


# --------------------------------------------------
# Tool Code Generation
# --------------------------------------------------

def _generate_tools(parsed: Dict[str, Any]) -> str:
    lines = [
        "from crewai.tools import tool",
        "",
    ]

    for tool_data in parsed.get("tools", []):
        fn_name = safe_name(tool_data["id"])
        description = (
            tool_data.get("description")
            or tool_data.get("title")
            or "CrewAI Tool"
        )

        lines.append(f"@tool('{fn_name}')")
        lines.append(f"def {fn_name}(input: str) -> str:")
        lines.append(
            textwrap.indent(
                f'""" {description} """\n'
                "return f\"[Tool stub] Executed with input: {input}\"",
                "    ",
            )
        )
        lines.append("")

    return "\n".join(lines)


# --------------------------------------------------
# Agent Code Generation
# --------------------------------------------------

def _generate_agents(parsed: Dict[str, Any]) -> str:
    lines = [
        "from crewai import Agent",
        "",
    ]

    for agent in parsed.get("agents", []):
        var = safe_name(agent["id"])

        role = agent.get("role") or agent.get("title") or "LLM Agent"
        goal = agent.get("goal_title") or "Complete assigned tasks"
        backstory = agent.get("description") or ""

        tool_vars = [safe_name(t) for t in agent.get("tools", [])]

        lines.append(f"{var} = Agent(")
        lines.append(f"    role={role!r},")
        lines.append(f"    goal={goal!r},")
        lines.append(f"    backstory={backstory!r},")
        lines.append(f"    tools=[{', '.join(tool_vars)}],")
        lines.append("    verbose=True")
        lines.append(")")
        lines.append("")

    return "\n".join(lines)


# --------------------------------------------------
# Task Code Generation (CORE FIXES HERE)
# --------------------------------------------------

def _generate_tasks(parsed: Dict[str, Any]) -> str:
    lines = [
        "from crewai import Task",
        "",
    ]

    # Prompt lookup
    prompt_lookup = {
        p["id"]: p for p in parsed.get("prompts", [])
    }

    for task in parsed.get("tasks", []):
        var = safe_name(task["id"])
        agent_var = safe_name(task.get("assigned_agent"))

        # ---- Task title (FIXES CrewAI naming bug)
        task_title = task.get("title") or safe_name(task["id"])

        # ---- Base description
        base_description = task.get("description", "").strip()

        # ---- Prompt injection
        prompt_blocks = []
        for prompt_id in task.get("prompts", []):
            prompt = prompt_lookup.get(prompt_id)
            if not prompt:
                continue

            if prompt.get("instruction"):
                prompt_blocks.append(
                    "INSTRUCTIONS:\n" + prompt["instruction"]
                )

            if prompt.get("input_data"):
                prompt_blocks.append(
                    "INPUTS:\n" + prompt["input_data"]
                )

            if prompt.get("output_indicator"):
                prompt_blocks.append(
                    "OUTPUT REQUIREMENTS:\n" + prompt["output_indicator"]
                )

        # ---- Output materialisation contract (GENERIC)
        output_kind = infer_output_kind(task)

        output_contract = (
            "OUTPUT CONTRACT:\n"
            f"- Output format: {output_kind}\n"
            "- Produce fully instantiated content\n"
            "- Do NOT explain ontology classes, RDF, schemas, or models\n"
            "- Do NOT include commentary, metadata, or explanations\n"
        )

        # ---- Final task description (compiler invariant)
        full_description = "\n\n".join(
            part for part in [
                f"TASK: {task_title}",
                base_description,
                *prompt_blocks,
                output_contract,
            ] if part
        )

        # ---- Expected output (CrewAI requirement)
        expected = task.get("expected_output")
        if not expected:
            if task.get("produced_resources"):
                expected = (
                    "Produce resource(s): "
                    + ", ".join(task["produced_resources"])
                )
            elif base_description:
                expected = f"Completed task: {task_title}"
            else:
                expected = "Task completed successfully."

        # ---- Emit Task
        lines.append(f"{var} = Task(")
        lines.append(f"    description={full_description!r},")
        lines.append(f"    expected_output={expected!r},")
        lines.append(f"    agent={agent_var}")
        lines.append(")")
        lines.append("")

    return "\n".join(lines)


# --------------------------------------------------
# Workflow Ordering
# --------------------------------------------------

def _generate_task_list(parsed: Dict[str, Any]) -> str:
    steps = sorted(
        parsed.get("workflow_steps", []),
        key=lambda s: s.get("step_order", 0),
    )

    ordered = []
    for step in steps:
        task_id = step.get("associated_task")
        if task_id:
            ordered.append(safe_name(task_id))

    if not ordered:
        ordered = [safe_name(t["id"]) for t in parsed.get("tasks", [])]

    return f"tasks = [{', '.join(ordered)}]"


# --------------------------------------------------
# Crew + Main
# --------------------------------------------------

def _generate_crew(parsed: Dict[str, Any]) -> str:
    agent_vars = [safe_name(a["id"]) for a in parsed.get("agents", [])]

    return f"""
from crewai import Crew

def main():
    crew = Crew(
        agents=[{', '.join(agent_vars)}],
        tasks=tasks,
        verbose=True
    )
    crew.kickoff()

if __name__ == "__main__":
    main()
"""


# --------------------------------------------------
# Public API
# --------------------------------------------------

def generate_crewai_code(parsed: Dict[str, Any]) -> str:
    """
    Generate executable CrewAI Python code from parsed AgentO KG.
    """

    sections = [
        "# =========================================================",
        "# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY",
        "# Source: AgentO Knowledge Graph",
        "# =========================================================",
        "",
        _generate_tools(parsed),
        _generate_agents(parsed),
        _generate_tasks(parsed),
        _generate_task_list(parsed),
        _generate_crew(parsed),
    ]

    return "\n\n".join(sections)


# --------------------------------------------------
# Quick test
# --------------------------------------------------

if __name__ == "__main__":
    import sys
    from parser import parse_kg
    import os

    input_file = sys.argv[1] if len(sys.argv) > 1 else "kg_g3/crewai/email_auto_responder_flow.rdf"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "output/crewai_generated.py"

    try:
        print(f"[INFO] Parsing KG from: {input_file}")
        parsed = parse_kg(input_file)

        print(f"[INFO] Generating CrewAI code...")
        code = generate_crewai_code(parsed)

        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(code)

        print(f"[INFO] CrewAI code generated → {output_file}")
        print("[INFO] Summary:")
        print(f"       - Agents: {len(parsed.get('agents', []))}")
        print(f"       - Tasks: {len(parsed.get('tasks', []))}")
        print(f"       - Tools: {len(parsed.get('tools', []))}")
        print(f"       - Teams: {len(parsed.get('teams', []))}")

    except Exception as e:
        print(f"[ERROR] Failed to generate code: {e}")
        import traceback
        traceback.print_exc()