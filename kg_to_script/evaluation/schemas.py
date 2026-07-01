"""Shared evaluation data structures."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Set, Tuple


@dataclass(frozen=True)
class EvaluationElement:
    """A KG/code element that can participate in OEC matching."""

    category: str
    name: str
    aliases: Tuple[str, ...] = ()
    important: bool = False
    details: Tuple[Tuple[str, str], ...] = ()

    @property
    def key(self) -> Tuple[str, str]:
        return (self.category, self.name)


@dataclass
class GraphSpec:
    """Minimal directed graph representation for workflow comparison."""

    nodes: Set[str] = field(default_factory=set)
    edges: Set[Tuple[str, str]] = field(default_factory=set)


@dataclass
class ExtractionResult:
    """Static extraction result from either KG or generated code."""

    elements: List[EvaluationElement] = field(default_factory=list)
    graph: GraphSpec = field(default_factory=GraphSpec)
    source_tokens: Set[str] = field(default_factory=set)
    source_text: str = ""
    metadata: Dict[str, str] = field(default_factory=dict)
