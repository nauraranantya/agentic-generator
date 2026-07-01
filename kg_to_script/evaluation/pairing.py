"""Pair input KG files with generated project directories."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, List, Tuple

from .config import FrameworkConfig


def project_name_from_kg(kg_path: Path) -> str:
    return kg_path.stem.replace("_instances", "")


def pair_projects(config: FrameworkConfig) -> List[Tuple[Path, Path, str]]:
    pairs = []
    if not config.kg_dir.exists():
        return pairs
    for kg_path in sorted(config.kg_dir.glob(config.kg_glob)):
        project_name = project_name_from_kg(kg_path)
        pairs.append((kg_path, config.output_dir / project_name, project_name))
    return pairs
