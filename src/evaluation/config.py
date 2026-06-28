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
    gt_dir: Path
    ext: str
    kg_glob: str = "*.ttl"


def framework_configs(root: Path) -> Dict[str, FrameworkConfig]:
    return {
        "crewai": FrameworkConfig(
            name="CrewAI",
            kg_dir=root / "kgs_original" / "CrewAI",
            output_dir=root / "output_files" / "output_crewai",
            gt_dir=root / "GT_scripts" / "CrewAI",
            ext=".py",
        ),
        "autogen": FrameworkConfig(
            name="AutoGen",
            kg_dir=root / "kgs_original" / "AutoGen",
            output_dir=root / "output_files" / "output_autogen",
            gt_dir=root / "GT_scripts" / "AutoGen",
            ext=".py",
        ),
        "langgraph": FrameworkConfig(
            name="LangGraph",
            kg_dir=root / "kgs_original" / "LangGraph",
            output_dir=root / "output_files" / "output_langgraph",
            gt_dir=root / "GT_scripts" / "LangGraph",
            ext=".ts",
        ),
        "mastra": FrameworkConfig(
            name="Mastra",
            kg_dir=root / "kgs_original" / "Mastra AI",
            output_dir=root / "output_files" / "output_mastra",
            gt_dir=root / "GT_scripts" / "Mastra AI",
            ext=".ts",
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
