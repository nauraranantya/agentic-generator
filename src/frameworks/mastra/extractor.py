"""Deprecated compatibility wrapper for Mastra extraction.

Mastra now relies on framework-agnostic extraction in ``src.core.extractor`` and
maps the canonical ``AgenticProject`` through ``src.frameworks.mastra.adapter``.
"""

from __future__ import annotations

import warnings

from ...core.extractor import extract_project
from .adapter import adapt
from .models import MastraProject


def extract_mastra_project(ttl_path: str) -> MastraProject:
    """Compatibility entrypoint returning a MastraProject.

    New call path: ``adapt(extract_project(ttl_path))``.
    """
    warnings.warn(
        "src.frameworks.mastra.extractor.extract_mastra_project is deprecated; use "
        "adapt(extract_project(...)) instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return adapt(extract_project(ttl_path))
