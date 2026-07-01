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
    # Compute repo root dynamically to prevent path issues when running CLI from different locations
    repo_root = Path(__file__).resolve().parent.parent
    return {
        "crewai": FrameworkConfig(
            name="CrewAI",
            kg_dir=repo_root / ".." / "script_to_kg" / "generated_kgs" / "CrewAI",
            output_dir=repo_root / "generated_projects" / "output_crewai",
            gt_dir=repo_root / ".." / "script_to_kg" / "ground_truth_scripts" / "CrewAI",
            ext=".py",
        ),
        "autogen": FrameworkConfig(
            name="AutoGen",
            kg_dir=repo_root / ".." / "script_to_kg" / "generated_kgs" / "AutoGen",
            output_dir=repo_root / "generated_projects" / "output_autogen",
            gt_dir=repo_root / ".." / "script_to_kg" / "ground_truth_scripts" / "AutoGen",
            ext=".py",
        ),
        "langgraph": FrameworkConfig(
            name="LangGraph",
            kg_dir=repo_root / ".." / "script_to_kg" / "generated_kgs" / "LangGraph",
            output_dir=repo_root / "generated_projects" / "output_langgraph",
            gt_dir=repo_root / ".." / "script_to_kg" / "ground_truth_scripts" / "LangGraph",
            ext=".ts",
        ),
        "mastra": FrameworkConfig(
            name="Mastra",
            kg_dir=repo_root / ".." / "script_to_kg" / "generated_kgs" / "Mastra AI",
            output_dir=repo_root / "generated_projects" / "output_mastra",
            gt_dir=repo_root / ".." / "script_to_kg" / "ground_truth_scripts" / "Mastra AI",
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
