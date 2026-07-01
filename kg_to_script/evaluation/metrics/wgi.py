"""Workflow Graph Isomorphism / similarity metric."""

from __future__ import annotations

from collections import Counter
from typing import Dict, Tuple

from ..schemas import ExtractionResult, GraphSpec


def calculate_wgi(kg: ExtractionResult, code: ExtractionResult) -> Dict[str, object]:
    kg_graph = kg.graph
    code_graph = code.graph

    missing_nodes = sorted(kg_graph.nodes - code_graph.nodes)
    extra_nodes = sorted(code_graph.nodes - kg_graph.nodes)
    missing_edges = sorted(kg_graph.edges - code_graph.edges)
    extra_edges = sorted(code_graph.edges - kg_graph.edges)

    edge_intersection = len(kg_graph.edges & code_graph.edges)
    precision = edge_intersection / len(code_graph.edges) if code_graph.edges else (1.0 if not kg_graph.edges else 0.0)
    recall = edge_intersection / len(kg_graph.edges) if kg_graph.edges else (1.0 if not code_graph.edges else 0.0)
    edge_f1 = (2 * precision * recall / (precision + recall)) if precision + recall else 0.0

    edit_operations = len(missing_nodes) + len(extra_nodes) + len(missing_edges) + len(extra_edges)
    normalizer = max(1, len(kg_graph.nodes | code_graph.nodes) + len(kg_graph.edges | code_graph.edges))
    labeled_normalized_edit_distance = edit_operations / normalizer
    labeled_score = max(0.0, 1.0 - labeled_normalized_edit_distance)

    topology_score, topology_edit_distance, topology_isomorphic = _topology_score(kg_graph, code_graph)
    score = max(labeled_score, topology_score)

    return {
        "score": score,
        "normalized_graph_edit_distance": min(labeled_normalized_edit_distance, topology_edit_distance),
        "labeled_score": labeled_score,
        "topology_score": topology_score,
        "labeled_normalized_graph_edit_distance": labeled_normalized_edit_distance,
        "topology_normalized_graph_edit_distance": topology_edit_distance,
        "exact_isomorphic": kg_graph.nodes == code_graph.nodes and kg_graph.edges == code_graph.edges,
        "topology_isomorphic": topology_isomorphic,
        "edge_precision": precision,
        "edge_recall": recall,
        "edge_f1": edge_f1,
        "kg_nodes": sorted(kg_graph.nodes),
        "code_nodes": sorted(code_graph.nodes),
        "kg_edges": [_edge_payload(edge) for edge in sorted(kg_graph.edges)],
        "code_edges": [_edge_payload(edge) for edge in sorted(code_graph.edges)],
        "missing_nodes": missing_nodes,
        "extra_nodes": extra_nodes,
        "missing_edges": [_edge_payload(edge) for edge in missing_edges],
        "extra_edges": [_edge_payload(edge) for edge in extra_edges],
    }


def _edge_payload(edge: Tuple[str, str]) -> Dict[str, str]:
    return {"source": edge[0], "target": edge[1]}


def _topology_score(kg_graph: GraphSpec, code_graph: GraphSpec) -> Tuple[float, float, bool]:
    """Approximate unlabeled directed-graph similarity using degree signatures."""
    if not kg_graph.nodes and not code_graph.nodes:
        return 1.0, 0.0, True

    kg_signature = _degree_signature(kg_graph)
    code_signature = _degree_signature(code_graph)
    signature_edits = _counter_distance(kg_signature, code_signature)
    edge_edits = abs(len(kg_graph.edges) - len(code_graph.edges))
    edits = signature_edits + edge_edits
    normalizer = max(
        1,
        max(len(kg_graph.nodes), len(code_graph.nodes)) + max(len(kg_graph.edges), len(code_graph.edges)),
    )
    distance = edits / normalizer
    return max(0.0, 1.0 - distance), distance, edits == 0


def _degree_signature(graph: GraphSpec) -> Counter[Tuple[int, int]]:
    in_degree = Counter(target for _, target in graph.edges)
    out_degree = Counter(source for source, _ in graph.edges)
    return Counter((in_degree[node], out_degree[node]) for node in graph.nodes)


def _counter_distance(left: Counter[Tuple[int, int]], right: Counter[Tuple[int, int]]) -> int:
    keys = set(left) | set(right)
    return sum(abs(left[key] - right[key]) for key in keys)
