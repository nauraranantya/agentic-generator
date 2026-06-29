"""Pure utility helpers for the agentO extraction pipeline.

All functions here are stateless and framework-agnostic.
"""

from __future__ import annotations

import re
from typing import Any, List

from rdflib import Graph


def s(val: Any) -> str:
    """Convert an rdflib term to a stripped string. Returns '' for None."""
    return str(val).strip() if val else ""


def safe_var(iri: str) -> str:
    """
    Convert an IRI fragment to a valid Python snake_case identifier.

    Examples:
        "http://…/onto#SeniorEngineerAgent" → "senior_engineer_agent"
        "http://…/onto#GPT4Tool"            → "gp_t4_tool"
    """
    if not iri:
        return "unnamed"
    name = iri.split("/")[-1].split("#")[-1]
    # Insert _ before uppercase runs: "SeniorEngineer" → "Senior_Engineer"
    name = re.sub(r"(?<=[a-z0-9])([A-Z])", r"_\1", name)
    name = re.sub(r"(?<=[A-Z])([A-Z][a-z])", r"_\1", name)
    name = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    name = re.sub(r"_+", "_", name).strip("_").lower()
    if not name:
        return "unnamed"
    if name[0].isdigit():
        name = f"_{name}"
    return name


def camel(s_: str) -> str:
    """Convert snake_case to CamelCase: 'game_builder_crew' → 'GameBuilderCrew'."""
    return "".join(w.capitalize() for w in s_.split("_"))


def extract_placeholders(text: str) -> List[str]:
    """Return unique {placeholder} variable names found in *text*, preserving order."""
    return list(dict.fromkeys(re.findall(r"\{(\w+)\}", text)))


from .normalizer import normalize_ttl


def load_graph(file_path: str) -> Graph:
    """Parse a Turtle (.ttl) file into an rdflib Graph after normalizing its content."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    normalized_content = normalize_ttl(content)
    
    g = Graph()
    g.parse(data=normalized_content, format="turtle")
    return g

