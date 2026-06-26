"""Evaluation configuration."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict


@dataclass(frozen=True)
class FrameworkConfig:
    name: str
    kg_dir: Path
    output_dir: Path
    kg_glob: str = "*.ttl"


def framework_configs(root: Path) -> Dict[str, FrameworkConfig]:
    return {
        "crewai": FrameworkConfig(
            name="CrewAI",
            kg_dir=root / "kgs_original" / "CrewAI",
            output_dir=root / "output_files" / "output_crewai",
        ),
        "autogen": FrameworkConfig(
            name="AutoGen",
            kg_dir=root / "kgs_original" / "AutoGen",
            output_dir=root / "output_files" / "output_autogen",
        ),
        "langgraph": FrameworkConfig(
            name="LangGraph",
            kg_dir=root / "kgs_original" / "LangGraph",
            output_dir=root / "output_files" / "output_langgraph",
        ),
        "mastra": FrameworkConfig(
            name="Mastra",
            kg_dir=root / "kgs_original" / "Mastra AI",
            output_dir=root / "output_files" / "output_mastra",
        ),
    }


IMPORTANT_CONFIG_KEYS = {
    "process",
    "temperature",
    "model",
    "model_name",
    "max_iter",
    "max_iters",
    "max_loops",
    "max_messages",
    "max_turns",
    "verbose",
    "allow_delegation",
    "memory",
    "human_input",
}
