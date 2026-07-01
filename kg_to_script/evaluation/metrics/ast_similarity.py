"""AST Similarity metric."""

from __future__ import annotations

import ast
import json
import subprocess
from pathlib import Path
from typing import Tuple, Set


class ASTNodeVisitor(ast.NodeVisitor):
    def __init__(self):
        self.nodes = []

    def generic_visit(self, node):
        self.nodes.append(type(node).__name__)
        super().generic_visit(node)


def calculate_ast_similarity(gen_code: str, gt_code: str, framework: str) -> float:
    """Calculates Jaccard similarity between the sets of AST node types for two codebases."""
    framework = framework.lower()
    
    if framework in {"crewai", "autogen"}:
        return _calculate_python_ast_similarity(gen_code, gt_code)
    elif framework in {"langgraph", "mastra"}:
        return _calculate_typescript_ast_similarity(gen_code, gt_code)
    
    return 0.0


def _calculate_python_ast_similarity(code_a: str, code_b: str) -> float:
    try:
        tree_a = ast.parse(code_a)
        tree_b = ast.parse(code_b)
        
        visitor_a = ASTNodeVisitor()
        visitor_b = ASTNodeVisitor()
        
        visitor_a.visit(tree_a)
        visitor_b.visit(tree_b)
        
        set_a, set_b = set(visitor_a.nodes), set(visitor_b.nodes)
        if not set_a or not set_b:
            return 0.0
        return len(set_a.intersection(set_b)) / len(set_a.union(set_b))
    except Exception:
        return 0.0


def _get_ts_ast_nodes(code: str) -> Set[str]:
    """Retrieves TS AST node kind names using a Node.js subprocess with typescript package."""
    try:
        node_script = """
const ts = require('typescript');
let code = '';
process.stdin.on('data', chunk => { code += chunk; });
process.stdin.on('end', () => {
    try {
        const sourceFile = ts.createSourceFile('temp.ts', code, ts.ScriptTarget.Latest, true);
        const kinds = new Set();
        function visit(node) {
            kinds.add(ts.SyntaxKind[node.kind]);
            ts.forEachChild(node, visit);
        }
        visit(sourceFile);
        console.log(JSON.stringify(Array.from(kinds)));
    } catch (e) {
        console.log('[]');
    }
});
"""
        res = subprocess.run(
            ["node", "-e", node_script],
            input=code,
            capture_output=True,
            text=True,
            timeout=5,
        )
        if res.returncode == 0:
            kinds = json.loads(res.stdout.strip())
            return set(kinds)
    except Exception:
        pass
    return set()


def _calculate_typescript_ast_similarity(code_a: str, code_b: str) -> float:
    set_a = _get_ts_ast_nodes(code_a)
    set_b = _get_ts_ast_nodes(code_b)
    if not set_a or not set_b:
        return 0.0
    return len(set_a.intersection(set_b)) / len(set_a.union(set_b))


def load_gt_code(gt_dir: Path, proj_name: str, framework: str) -> Tuple[bool, str]:
    """Loads Ground Truth code content depending on framework's file structure.
    
    Returns (gt_found, gt_code).
    """
    framework = framework.lower()
    
    if framework == "autogen":
        gt_file = gt_dir / f"{proj_name}.ipynb"
        if gt_file.exists():
            return True, _extract_code_from_ipynb(gt_file)
        return False, ""
        
    elif framework == "mastra":
        gt_folder = gt_dir / proj_name
        gt_file = gt_dir / f"{proj_name}.ts"
        if gt_folder.exists() and gt_folder.is_dir():
            return True, get_combined_source(gt_folder, ".ts")
        elif gt_file.exists():
            try:
                return True, gt_file.read_text(encoding="utf-8")
            except Exception:
                return False, ""
        return False, ""
        
    elif framework == "crewai":
        gt_folder = gt_dir / proj_name
        if gt_folder.exists() and gt_folder.is_dir():
            return True, get_combined_source(gt_folder, ".py")
        return False, ""
        
    elif framework == "langgraph":
        gt_folder = gt_dir / proj_name
        if gt_folder.exists() and gt_folder.is_dir():
            return True, get_combined_source(gt_folder, ".ts")
        return False, ""
        
    return False, ""


def _extract_code_from_ipynb(ipynb_path: Path) -> str:
    """Extracts python code lines from a Jupyter Notebook file."""
    try:
        with open(ipynb_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        code_lines = []
        for cell in data.get("cells", []):
            if cell.get("cell_type") == "code":
                source = cell.get("source", [])
                if isinstance(source, list):
                    code_lines.append("".join(source))
                elif isinstance(source, str):
                    code_lines.append(source)
        return "\n\n".join(code_lines)
    except Exception:
        return ""


def get_combined_source(directory: Path, extension: str) -> str:
    """Recursively combines the content of all files matching the extension under a directory."""
    content = []
    if not directory.exists():
        return ""
    for path in sorted(directory.rglob(f"*{extension}")):
        if any(part in path.parts for part in ("node_modules", ".agento-env", "__pycache__", ".pytest_cache", "dist", "build")):
            continue
        try:
            content.append(path.read_text(encoding="utf-8"))
        except Exception:
            pass
    return "\n\n".join(content)
