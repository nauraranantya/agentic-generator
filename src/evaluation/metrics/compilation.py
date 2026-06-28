"""Compilation/Syntax check metrics."""

from __future__ import annotations

import sys
import subprocess
from pathlib import Path


def compile_project(project_dir: Path, framework: str) -> bool:
    """Checks syntax compilation of the project based on the framework type.
    
    Returns True if compilation is successful, False otherwise.
    """
    framework = framework.lower()
    if framework in {"crewai", "autogen"}:
        return _compile_python_files(project_dir)
    elif framework in {"langgraph", "mastra"}:
        return _compile_typescript_files(project_dir)
    return True


def _compile_python_files(project_dir: Path) -> bool:
    """Runs py_compile on all Python files under the project directory."""
    success = True
    for path in project_dir.rglob("*.py"):
        if "__pycache__" in path.parts:
            continue
        try:
            res = subprocess.run(
                [sys.executable, "-m", "py_compile", str(path)],
                capture_output=True,
                text=True,
            )
            if res.returncode != 0:
                success = False
        except Exception:
            success = False
    return success


def _compile_typescript_files(project_dir: Path) -> bool:
    """Runs tsc compiler on the project directory if node_modules exists, otherwise defaults to True."""
    node_modules_path = project_dir / "node_modules"
    if node_modules_path.exists():
        try:
            res = subprocess.run(
                ["node", "node_modules/typescript/bin/tsc", "--noEmit"],
                cwd=project_dir,
                capture_output=True,
                text=True,
            )
            return res.returncode == 0
        except Exception:
            return False
    return True
