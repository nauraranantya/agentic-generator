"""Ontology Element Coverage metric."""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import Dict, Iterable, List, Set, Tuple

from ..schemas import EvaluationElement, ExtractionResult
from ..utils import normalize_name, token_set


RELATION_CATEGORIES = {
    "agent_tool",
    "agent_goal",
    "agent_llm",
    "agent_interaction",
    "agent_capability",
    "task_agent",
    "task_produces",
    "task_requires",
    "task_capability",
    "task_context",
    "tool_capability",
    "step_task",
}


import re

def calculate_oec(kg: ExtractionResult, code: ExtractionResult) -> Dict[str, object]:
    all_elements = kg.elements
    important_elements = [element for element in kg.elements if element.important]

    raw_words = re.findall(r"[a-zA-Z0-9]+", code.source_text or "")
    source_words = [w.lower() for w in raw_words if w]

    all_result = _score_elements(all_elements, code, source_words)
    important_result = _score_elements(important_elements, code, source_words)

    return {
        "all_extracted": all_result,
        "important_subset": important_result,
    }


def _score_elements(expected: List[EvaluationElement], code: ExtractionResult, source_words: List[str]) -> Dict[str, object]:
    matched = []
    missing = []
    category_totals: Counter[str] = Counter()
    category_matched: Counter[str] = Counter()

    code_index = _code_index(code)
    source_tokens = set(code.source_tokens)
    source_tokens.update(token_set(code.source_text))

    for element in expected:
        category_totals[element.category] += 1
        if _is_matched(element, code_index, source_tokens, source_words):
            matched.append(_element_payload(element))
            category_matched[element.category] += 1
        else:
            missing.append(_element_payload(element))

    denominator = len(expected)
    score = len(matched) / denominator if denominator else 1.0
    return {
        "score": score,
        "matched": len(matched),
        "total": denominator,
        "missing": missing,
        "by_category": _category_breakdown(category_totals, category_matched),
    }


def _code_index(code: ExtractionResult) -> Dict[str, Set[str]]:
    index: Dict[str, Set[str]] = defaultdict(set)
    for element in code.elements:
        index[element.category].add(element.name)
        index[element.category].update(element.aliases)
    return index


def _is_subsegment(sub: List[str], parent: List[str]) -> bool:
    if not sub:
        return False
    n = len(sub)
    for i in range(len(parent) - n + 1):
        if parent[i:i+n] == sub:
            return True
    return False


def _is_matched(element: EvaluationElement, code_index: Dict[str, Set[str]], source_tokens: Set[str], source_words: List[str]) -> bool:
    aliases = {element.name, *element.aliases}
    aliases = {normalize_name(alias) for alias in aliases if normalize_name(alias)}

    if element.category in RELATION_CATEGORIES:
        return _relation_is_matched(element, source_tokens)

    category_names = code_index.get(element.category, set())
    if aliases & category_names:
        return True

    # Fallback 1: exact token matching
    if any(alias in source_tokens for alias in aliases):
        return True

    # Fallback 2: space/underscore-insensitive contiguous phrase matching
    for alias in aliases:
        # Split alias into alphanumeric parts
        alias_words = [w.lower() for w in re.split(r"[^a-zA-Z0-9]+", alias) if w]
        if alias_words and _is_subsegment(alias_words, source_words):
            return True

    return False


def _relation_is_matched(element: EvaluationElement, source_tokens: Set[str]) -> bool:
    details = dict(element.details)
    source = normalize_name(details.get("source", ""))
    target = normalize_name(details.get("target", ""))
    if not source or not target:
        return False
    return source in source_tokens and target in source_tokens


def _category_breakdown(totals: Counter[str], matched: Counter[str]) -> Dict[str, Dict[str, float]]:
    breakdown = {}
    for category in sorted(totals):
        total = totals[category]
        matched_count = matched[category]
        breakdown[category] = {
            "score": matched_count / total if total else 1.0,
            "matched": matched_count,
            "total": total,
        }
    return breakdown


def _element_payload(element: EvaluationElement) -> Dict[str, object]:
    return {
        "category": element.category,
        "name": element.name,
        "important": element.important,
        "aliases": list(element.aliases),
        "details": dict(element.details),
    }
