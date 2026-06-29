"""Static extraction from generated framework code."""

from __future__ import annotations

import ast
import re
from pathlib import Path
from typing import Iterable, List, Optional

from ..schemas import EvaluationElement, ExtractionResult, GraphSpec
from ..utils import aliases_for, iter_text_files, normalize_name, read_project_text, token_set


def extract_code(project_dir: Path, framework: str) -> ExtractionResult:
    text = read_project_text(project_dir)
    elements = _extract_common_elements(text, project_dir, framework)
    graph = _extract_graph(text, project_dir, framework)
    return ExtractionResult(
        elements=_dedupe(elements),
        graph=graph,
        source_tokens=token_set(text),
        source_text=text,
        metadata={"project_dir": str(project_dir), "framework": framework},
    )


def _element(category: str, name: str, *aliases: object, important: bool = False) -> EvaluationElement:
    return EvaluationElement(category=category, name=normalize_name(name), aliases=aliases_for(name, *aliases), important=important)


def _extract_common_elements(text: str, project_dir: Path, framework: str) -> List[EvaluationElement]:
    elements: List[EvaluationElement] = []
    framework = framework.lower()

    if framework in {"crewai", "autogen"}:
        for path in iter_text_files(project_dir):
            if path.suffix == ".py":
                elements.extend(_extract_python_elements(path))

    if framework in {"langgraph", "mastra"}:
        elements.extend(_extract_typescript_elements(text, framework))

    # Config-like key/value strings are useful for OEC config matching.
    for key in re.findall(r"[\"']([a-zA-Z_][a-zA-Z0-9_\-]*(?:temperature|model|max|verbose|process|memory|delegation)[a-zA-Z0-9_\-]*)[\"']\s*[:=]", text):
        elements.append(_element("config", key, important=True))

    return elements


def _extract_python_elements(path: Path) -> List[EvaluationElement]:
    elements: List[EvaluationElement] = []
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except (SyntaxError, UnicodeDecodeError):
        return elements

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            decorators = {_decorator_name(dec) for dec in node.decorator_list}
            if "agent" in decorators:
                elements.append(_element("agent", node.name, important=True))
            if "task" in decorators:
                elements.append(_element("task", node.name, important=True))
            if "tool" in decorators:
                tool_name = _first_string_arg(node.decorator_list) or node.name
                elements.append(_element("tool", node.name, tool_name, important=True))

        if isinstance(node, ast.Assign):
            call = node.value if isinstance(node.value, ast.Call) else None
            call_name = _call_name(call) if call else ""
            for target in node.targets:
                target_name = _target_name(target)
                if not target_name:
                    continue
                if call_name in {"AssistantAgent", "UserProxyAgent", "Agent"}:
                    elements.append(_element("agent", target_name, _keyword_string(call, "name"), important=True))
                if call_name in {"FunctionTool", "Tool"}:
                    elements.append(_element("tool", target_name, _keyword_string(call, "name"), important=True))

    return elements


def _extract_typescript_elements(text: str, framework: str) -> List[EvaluationElement]:
    elements: List[EvaluationElement] = []

    if framework == "mastra":
        # Mastra-specific API patterns
        for match in re.finditer(r"(?:export\s+)?const\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*new\s+Agent\s*\(", text):
            elements.append(_element("agent", match.group(1), important=True))
        for match in re.finditer(r"(?:export\s+)?const\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*createStep\s*\(", text):
            elements.append(_element("task", match.group(1), important=True))
            elements.append(_element("workflow_step", match.group(1), important=True))
        for match in re.finditer(r"id\s*:\s*[\"']([^\"']+)[\"']", text):
            category = "workflow" if "workflow" in normalize_name(match.group(1)) else "workflow_step"
            elements.append(_element(category, match.group(1), important=True))
        for match in re.finditer(r"(?:export\s+)?const\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*createTool\s*\(", text):
            elements.append(_element("tool", match.group(1), important=True))
        for match in re.finditer(r"\.addNode\s*\(\s*[\"']([^\"']+)[\"']", text):
            elements.append(_element("workflow_step", match.group(1), important=True))

    elif framework == "langgraph":
        # Detect LLM-backed agents: new ChatOpenAI(...) or new ChatAnthropic(...)
        llm_instantiations = re.findall(
            r"new\s+(?:ChatOpenAI|ChatAnthropic)\s*\(", text
        )
        if llm_instantiations:
            # One agent per unique LLM instantiation scope — simplify to one agent element
            # per distinct async function that contains a model call.
            for match in re.finditer(
                r"async\s+function\s+([A-Za-z_][A-Za-z0-9_]*)\s*\([^)]*\)[^{]*\{[^}]*new\s+(?:ChatOpenAI|ChatAnthropic)",
                text,
                flags=re.S,
            ):
                elements.append(_element("agent", match.group(1), important=True))
            # If no named function bodies found (e.g., inline addNode), add a generic agent
            if not any(e.category == "agent" for e in elements):
                elements.append(_element("agent", "agent", important=True))

        # Detect workflow steps from .addNode("name", ...) calls — these are the
        # authoritative task/step identifiers in LangGraph code.
        for match in re.finditer(r"\.addNode\s*\(\s*[\"']([^\"']+)[\"']", text):
            node_name = match.group(1)
            elements.append(_element("task", node_name, important=True))
            elements.append(_element("workflow_step", node_name, important=True))

        # Detect tools from tool function definitions (named functions bound to agents)
        for match in re.finditer(r"(?:export\s+)?(?:async\s+)?function\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", text):
            fn_name = match.group(1)
            # Skip known node names (already captured above) and generic helpers
            if not any(fn_name == e.name for e in elements if e.category == "workflow_step"):
                elements.append(_element("tool", fn_name, important=True))

        # Detect the workflow itself from new StateGraph(...) instantiation
        for _ in re.finditer(r"new\s+StateGraph\s*\(", text):
            elements.append(_element("workflow", "workflow", important=True))
            break  # Only one workflow per file expected

    return elements



def _extract_graph(text: str, project_dir: Path, framework: str) -> GraphSpec:
    framework = framework.lower()
    if framework == "langgraph":
        return _extract_langgraph_graph(text)
    if framework == "mastra":
        return _extract_mastra_graph(text, project_dir)
    if framework == "autogen":
        return _extract_autogen_graph(text)
    if framework == "crewai":
        return _extract_crewai_graph(project_dir)
    return GraphSpec()


def _extract_langgraph_graph(text: str) -> GraphSpec:
    graph = GraphSpec()
    for source, target in re.findall(r"\.addEdge\s*\(\s*([^,]+?)\s*,\s*([^\)]+?)\s*\)", text):
        source_name = _clean_graph_name(source)
        target_name = _clean_graph_name(target)
        if source_name not in {"start", "end"}:
            graph.nodes.add(source_name)
        if target_name not in {"start", "end"}:
            graph.nodes.add(target_name)
        if source_name not in {"start", "end"} and target_name not in {"start", "end"}:
            graph.edges.add((source_name, target_name))

    for source, body in re.findall(r"\.addConditionalEdges\s*\(\s*[\"']([^\"']+)[\"']\s*,[^\[]*\[([^\]]+)\]", text, flags=re.S):
        source_name = normalize_name(source)
        graph.nodes.add(source_name)
        for target in re.findall(r"[\"']([^\"']+)[\"']", body):
            target_name = normalize_name(target)
            graph.nodes.add(target_name)
            graph.edges.add((source_name, target_name))
    return graph


def _extract_mastra_graph(text: str, project_dir: Optional[Path] = None) -> GraphSpec:
    """Extract Mastra workflow graph.

    Processes each workflow TypeScript file individually so that `.then()` chains
    from different workflows are never connected to each other (which would create
    false cross-workflow edges and tank WGI scores).

    Search order for workflow files:
      1. <project_dir>/src/mastra/workflows/*.ts
      2. <project_dir>/src/workflows/*.ts
      3. Fall back to searching the full concatenated project text.
    """
    graph = GraphSpec()

    # Try to find individual workflow files.
    workflow_files: List[Path] = []
    if project_dir and project_dir.is_dir():
        for candidate_dir in (
            project_dir / "src" / "mastra" / "workflows",
            project_dir / "src" / "workflows",
            project_dir / "workflows",
        ):
            if candidate_dir.is_dir():
                workflow_files = sorted(candidate_dir.glob("*.ts"))
                break

    def _parse_workflow_text(wf_text: str) -> None:
        """Parse a single workflow file and merge results into graph."""
        steps = [normalize_name(s) for s in re.findall(r"\.then\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)", wf_text)]
        if steps:
            graph.nodes.update(steps)
            for src, tgt in zip(steps, steps[1:]):
                graph.edges.add((src, tgt))
            return
        # No .then() chains — fall back to `steps: [...]` array
        for body in re.findall(r"steps\s*:\s*\[([^\]]+)\]", wf_text, flags=re.S):
            step_names = [normalize_name(s) for s in re.findall(r"[A-Za-z_][A-Za-z0-9_]*", body)]
            if step_names:
                graph.nodes.update(step_names)
                for src, tgt in zip(step_names, step_names[1:]):
                    graph.edges.add((src, tgt))

    if workflow_files:
        for wf_file in workflow_files:
            try:
                wf_text = wf_file.read_text(encoding="utf-8", errors="replace")
                _parse_workflow_text(wf_text)
            except OSError:
                continue
    else:
        # No per-file isolation possible — process full text as before.
        _parse_workflow_text(text)

    return graph


def _extract_autogen_graph(text: str) -> GraphSpec:
    graph = GraphSpec()
    
    # 1. Parse structured workflow comments if present
    step_matches = re.findall(r"#\s*Workflow Step:\s*([a-zA-Z0-9_]+)", text)
    edge_matches = re.findall(r"#\s*Workflow Edge:\s*([a-zA-Z0-9_]+)\s*->\s*([a-zA-Z0-9_]+)", text)
    
    if step_matches:
        for step in step_matches:
            graph.nodes.add(normalize_name(step))
        for src, tgt in edge_matches:
            graph.edges.add((normalize_name(src), normalize_name(tgt)))
        return graph

    # 2. Fallback to legacy sender/recipient parser
    for sender, recipient in re.findall(r"sender:\s*([a-zA-Z_][a-zA-Z0-9_]*);\s*recipient:\s*([a-zA-Z_][a-zA-Z0-9_]*)", text):
        source = normalize_name(sender)
        target = normalize_name(recipient)
        graph.nodes.update({source, target})
        graph.edges.add((source, target))

    # 3. Fallback to participants list
    participants_match = re.search(r"participants\s*=\s*\[([^\]]+)\]", text, flags=re.S)
    if participants_match and not graph.edges:
        participants = [normalize_name(name) for name in re.findall(r"[a-zA-Z_][a-zA-Z0-9_]*", participants_match.group(1))]
        graph.nodes.update(participants)
        for source, target in zip(participants, participants[1:]):
            graph.edges.add((source, target))
    return graph


def _extract_crewai_graph(project_dir: Path) -> GraphSpec:
    graph = GraphSpec()
    for path in iter_text_files(project_dir):
        if path.suffix != ".py":
            continue
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))
        except (SyntaxError, UnicodeDecodeError):
            continue
        task_names: List[str] = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if "task" in {_decorator_name(dec) for dec in node.decorator_list}:
                    task_names.append(normalize_name(node.name))
        graph.nodes.update(task_names)
        for source, target in zip(task_names, task_names[1:]):
            graph.edges.add((source, target))
    return graph


def _decorator_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Call):
        return _decorator_name(node.func)
    if isinstance(node, ast.Attribute):
        return node.attr
    return ""


def _call_name(node: Optional[ast.Call]) -> str:
    if node is None:
        return ""
    if isinstance(node.func, ast.Name):
        return node.func.id
    if isinstance(node.func, ast.Attribute):
        return node.func.attr
    return ""


def _target_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    return ""


def _keyword_string(call: Optional[ast.Call], key: str) -> str:
    if call is None:
        return ""
    for kw in call.keywords:
        if kw.arg == key and isinstance(kw.value, ast.Constant):
            return str(kw.value.value)
    return ""


def _first_string_arg(decorators: Iterable[ast.AST]) -> str:
    for decorator in decorators:
        if isinstance(decorator, ast.Call):
            for arg in decorator.args:
                if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                    return arg.value
    return ""


def _clean_graph_name(value: str) -> str:
    value = value.strip().strip(";,")
    value = value.strip("\"'")
    return normalize_name(value)


def _dedupe(elements: List[EvaluationElement]) -> List[EvaluationElement]:
    seen = set()
    unique = []
    for element in elements:
        if not element.name:
            continue
        key = (element.category, element.name)
        if key in seen:
            continue
        seen.add(key)
        unique.append(element)
    return unique
