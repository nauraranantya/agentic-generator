"""Small helpers shared by evaluation modules."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable, Iterator, Set


TEXT_EXTENSIONS = {".py", ".ts", ".tsx", ".js", ".jsx", ".yaml", ".yml", ".json", ".md"}
SKIP_PARTS = {"node_modules", "__pycache__", ".pytest_cache", ".agento-env", "dist", "build"}


def normalize_name(value: object) -> str:
    text = str(value or "")
    # camelCase boundary: aB → a_B
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", text)
    # letter → digit boundary: stepA2 → stepA_2, task2 → task_2
    text = re.sub(r"([a-zA-Z])(\d)", r"\1_\2", text)
    # digit → letter boundary: 2step → 2_step
    text = re.sub(r"(\d)([a-zA-Z])", r"\1_\2", text)
    text = text.replace("-", "_").replace(" ", "_")
    text = re.sub(r"[^a-zA-Z0-9_]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text.lower()


def local_name(iri: str) -> str:
    if not iri:
        return ""
    return iri.rsplit("#", 1)[-1].rsplit("/", 1)[-1]


def token_set(text: str) -> Set[str]:
    # Include colon-joined identifiers (e.g. "task:my-step-2") in addition to plain words
    raw = re.findall(r"[a-zA-Z_][a-zA-Z0-9_:\-]*", text or "")
    tokens = {normalize_name(token) for token in raw if token}
    compact = normalize_name(text)
    if compact:
        tokens.add(compact)
    return tokens


def read_project_text(project_dir: Path) -> str:
    parts = []
    for path in iter_text_files(project_dir):
        try:
            parts.append(path.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            continue
    return "\n\n".join(parts)


def iter_text_files(project_dir: Path) -> Iterator[Path]:
    if not project_dir.exists():
        return
    for path in sorted(project_dir.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.suffix in TEXT_EXTENSIONS:
            yield path


def aliases_for(*values: object) -> tuple[str, ...]:
    aliases = []
    seen = set()
    for value in values:
        if value is None:
            continue
        text = str(value).strip()
        if not text:
            continue
        candidates = {text, normalize_name(text), local_name(text), normalize_name(local_name(text))}
        for candidate in candidates:
            normalized = normalize_name(candidate)
            if normalized and normalized not in seen:
                seen.add(normalized)
                aliases.append(normalized)
    return tuple(aliases)


def first_non_empty(values: Iterable[object], fallback: str = "") -> str:
    for value in values:
        text = str(value or "").strip()
        if text:
            return text
    return fallback
