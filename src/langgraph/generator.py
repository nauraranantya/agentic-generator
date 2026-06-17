"""
Layer 3 – File Generation (LangGraph)

Generates a complete LangGraph project directory from a LangGraphProject IR:
  - graph.py            (via Jinja2 — pattern-specific template)
  - main.py             (via Jinja2)
  - config/inputs.yaml  (via manual YAML building)
  - .env.example        (plain text)
  - requirements.txt    (plain text)

Design decisions:
  - Python files use Jinja2 templates loaded from the templates/ directory.
    Templates are NOT embedded in this file (use FileSystemLoader, not DictLoader).
  - YAML files are built manually so we avoid adding PyYAML as a required
    dependency for such a small output.
  - The pattern (linear / tool_calling / supervisor) is detected automatically
    from the LangGraphProject IR via the `pattern_type` property.
  - graph.py is always named `graph.py` so that `main.py` can do a stable
    `from graph import app` regardless of the pattern used.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from typing import Any, Dict, List

from jinja2 import Environment, FileSystemLoader

from ..core.models import (
    LangGraphAgentModel,
    LangGraphProject,
)


# ─────────────────────── Jinja2 setup ───────────────────────

def _create_jinja_env() -> Environment:
    """Create a Jinja2 environment that loads templates from the templates/ directory."""
    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    return Environment(
        loader=FileSystemLoader(template_dir),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )


# ─────────────────────── Context builders ───────────────────────

def _build_graph_context(project: LangGraphProject) -> Dict[str, Any]:
    """Build the complete Jinja2 template context for graph.py."""
    agents = project.agents
    if not agents:
        agents = [LangGraphAgentModel(
            iri="default-agent",
            var_name="agent",
            role="assistant",
            prompt="You are a helpful assistant.",
            model_name="gpt-4o-mini",
        )]

    # Filter out meta-nodes (e.g., nodes whose IRI ends with "Graph")
    nodes = [n for n in project.nodes if not n.iri.endswith("Graph")] or project.nodes

    return {
        "graph_name": project.name,
        "tools": project.tools,
        "agents": agents,
        "nodes": nodes,
        "edges": project.edges,
        "goals": project.goals,
        "objectives": project.objectives,
        "human_agents": project.human_agents,
        "environments": project.environments,
        "capabilities": project.capabilities,
        "resources": project.resources,
        "constraints": project.constraints,
        "tasks": project.tasks,
    }


def _build_main_context(project: LangGraphProject) -> Dict[str, Any]:
    """Build the complete Jinja2 template context for main.py."""
    return {
        "graph_name": project.name,
        "input_variables": project.input_variables,
    }


# ─────────────────────── YAML helpers ───────────────────────

def _append_yaml_scalar(lines: List[str], key: str, value: str) -> None:
    """Append a YAML scalar entry (key: value) to *lines*."""
    if "\n" in value or len(value) > 100:
        lines.append(f"{key}: |")
        for vline in value.split("\n"):
            lines.append(f"  {vline}")
    else:
        needs_quote = any(c in value for c in ":{},[]*#?|-><!%@`&")
        if needs_quote:
            escaped = value.replace('"', '\\"')
            lines.append(f'{key}: "{escaped}"')
        else:
            lines.append(f"{key}: {value}")


def _append_yaml_list_item(lines: List[str], value: str) -> None:
    """Append a YAML list item (- value) to *lines*."""
    if "\n" in value or len(value) > 100:
        lines.append("  - |")
        for vline in value.split("\n"):
            lines.append(f"    {vline}")
    else:
        needs_quote = any(c in value for c in ":{},[]*#?|-><!%@`&")
        if needs_quote:
            escaped = value.replace('"', '\\"')
            lines.append(f'  - "{escaped}"')
        else:
            lines.append(f"  - {value}")


# ─────────────────────── Content builders ───────────────────────

def build_inputs_yaml(project: LangGraphProject) -> str:
    """
    Build config/inputs.yaml content from the LangGraphProject IR.

    Each input variable becomes a top-level key.  When there are multiple
    example values from the KG (default + alternatives) the key maps to a
    YAML *list* — the first item is used as the runtime default by main.py.
    When only a single value exists the key maps to a scalar.
    """
    if not project.input_variables:
        return "# No runtime inputs required for this graph.\n"

    lines: List[str] = [
        "# Runtime inputs for the LangGraph app.",
        "# Edit values below before running python main.py.",
        "#",
        "# When a key maps to a list, main.py uses the FIRST item as the",
        "# runtime value.  Reorder or edit the list to choose a different example.",
        "#",
        "# Variables with no concrete value (defaults to empty string) are",
        "# required - you must provide a value before running.",
        "",
    ]

    for var in project.input_variables:
        all_values: List[str] = []
        if var.has_default and var.default_value:
            all_values.append(var.default_value)
        all_values.extend(var.alternative_values)

        if not all_values:
            lines.append(f'{var.name}: ""  # required - provide a value before running')
            continue

        if len(all_values) == 1:
            _append_yaml_scalar(lines, var.name, all_values[0])
        else:
            lines.append(f"{var.name}:")
            for val in all_values:
                _append_yaml_list_item(lines, val)

    lines.append("")
    return "\n".join(lines)


def build_env_example(project: LangGraphProject) -> str:
    """
    Generate .env.example content from a LangGraphProject IR.

    OPENAI_API_KEY is always included.  Optional overrides for base URL
    and model are shown as commented-out examples.
    """
    lines = [
        "# .env.example – copy to .env and fill in your actual keys",
        "# Never commit the real .env file to version control.",
        "",
        "# LLM API Key (required)",
        "OPENAI_API_KEY=your_openai_api_key_here",
        "",
        "# Optional: override the OpenAI base URL (e.g. for Azure, DeepInfra, etc.)",
        "# OPENAI_API_BASE=https://api.openai.com/v1",
        "",
        "# Optional: override the default model",
        "# LLM_MODEL=gpt-4o-mini",
        "",
    ]
    return "\n".join(lines)


def build_requirements_txt() -> str:
    """Return the contents of requirements.txt for a LangGraph project."""
    return (
        "langgraph>=0.0.26\n"
        "langchain-openai>=0.1.1\n"
        "langchain-core\n"
        "python-dotenv\n"
        "pyyaml>=6.0\n"
    )


def build_manifest(output_dir: str, pattern: str) -> dict:
    """Build a manifest dict describing the generated project."""
    generated_files = []
    for root, _, files in os.walk(output_dir):
        for file in files:
            if file == "manifest.json":
                continue
            abs_path = os.path.join(root, file)
            rel_path = os.path.relpath(abs_path, output_dir)
            generated_files.append(rel_path.replace("\\", "/"))

    return {
        "framework": "langgraph",
        "pattern": pattern,
        "generated_files": sorted(generated_files),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


# ─────────────────────── Public API ───────────────────────

def generate_project(project: LangGraphProject, output_dir: str) -> str:
    """
    Generate a complete LangGraph project directory from a LangGraphProject IR.

    Output structure:
        <output_dir>/
        ├── .env.example
        ├── requirements.txt
        ├── config/
        │   └── inputs.yaml     ← runtime inputs (from KickoffInputBundle)
        ├── graph.py            ← the compiled StateGraph app
        ├── main.py             ← entry point
        └── manifest.json       ← generation metadata

    Returns:
        The output directory path.
    """
    # ── Create directory structure ──
    config_dir = os.path.join(output_dir, "config")
    os.makedirs(config_dir, exist_ok=True)

    pattern = project.pattern_type

    # ── Layer 3A: Python generation (Jinja2) ──
    env = _create_jinja_env()

    # graph.py — always named graph.py for a stable import in main.py
    graph_template = env.get_template(f"{pattern}.py.j2")
    graph_ctx = _build_graph_context(project)
    graph_code = graph_template.render(**graph_ctx)
    with open(os.path.join(output_dir, "graph.py"), "w", encoding="utf-8") as f:
        f.write(graph_code.strip() + "\n")

    # main.py
    main_template = env.get_template("main.py.j2")
    main_ctx = _build_main_context(project)
    main_code = main_template.render(**main_ctx)
    with open(os.path.join(output_dir, "main.py"), "w", encoding="utf-8") as f:
        f.write(main_code.strip() + "\n")

    # ── Layer 3B: YAML / plain-text generation ──
    with open(os.path.join(config_dir, "inputs.yaml"), "w", encoding="utf-8") as f:
        f.write(build_inputs_yaml(project))

    with open(os.path.join(output_dir, ".env.example"), "w", encoding="utf-8") as f:
        f.write(build_env_example(project))

    with open(os.path.join(output_dir, "requirements.txt"), "w", encoding="utf-8") as f:
        f.write(build_requirements_txt())

    # ── Manifest ──
    manifest = build_manifest(output_dir, pattern)
    with open(os.path.join(output_dir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(
        f"  [Generated] {output_dir}/ "
        f"(graph.py [{pattern}], main.py, inputs.yaml, .env.example, requirements.txt)"
    )

    return output_dir