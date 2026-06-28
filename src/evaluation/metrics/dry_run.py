"""Dry run execution metrics for python projects."""

from __future__ import annotations

import os
import sys
import subprocess
from pathlib import Path


def dry_run_project(project_dir: Path, framework: str) -> dict:
    """Executes a dry-run check on python project's main.py using a dummy API key.
    
    Returns a dict with 'status' and 'output'.
    """
    framework = framework.lower()
    if framework in {"crewai", "autogen"}:
        main_py = project_dir / "main.py"
        if main_py.exists():
            return _dry_run_python_project(main_py)
    return {"status": "N/A", "output": ""}


def _dry_run_python_project(main_py_path: Path) -> dict:
    """Runs the python script with a dummy OpenAI key to check for runtime initialization errors."""
    env = os.environ.copy()
    env["OPENAI_API_KEY"] = "sk-dummy"
    try:
        res = subprocess.run(
            [sys.executable, str(main_py_path.resolve())],
            cwd=str(main_py_path.parent.resolve()),
            env=env,
            capture_output=True,
            text=True,
            timeout=10,
        )
        stdout = res.stdout
        stderr = res.stderr
        exit_code = res.returncode
        
        error_msg = stderr.strip() or stdout.strip()
        
        # Success if it runs fine or hits authentic authentication error due to sk-dummy
        success_indicators = [
            "AuthenticationError", 
            "Incorrect API key", 
            "401", 
            "unauthorized", 
            "api_key",
            "APIKeyError",
            "APIConnectionError"
        ]
        
        is_success = any(ind in error_msg for ind in success_indicators) or (exit_code == 0)
        
        if is_success:
            return {"status": "SUCCESS_DUMMY", "output": ""}
        else:
            # Classify error type
            error_type = "OTHER_ERROR"
            for line in error_msg.splitlines():
                if "NameError:" in line:
                    error_type = "NAME_ERROR"
                    break
                elif "SyntaxError:" in line:
                    error_type = "SYNTAX_ERROR"
                    break
                elif "ImportError:" in line or "ModuleNotFoundError:" in line:
                    error_type = "IMPORT_ERROR"
                    break
                elif "TypeError:" in line:
                    error_type = "TYPE_ERROR"
                    break
                elif "ValueError:" in line:
                    error_type = "VALUE_ERROR"
                    break
            
            details = "\n".join(error_msg.splitlines()[-5:])
            return {"status": error_type, "output": details}
            
    except subprocess.TimeoutExpired:
        return {"status": "TIMEOUT", "output": "Proyek timeout setelah 10 detik"}
    except Exception as e:
        return {"status": "OTHER_ERROR", "output": str(e)}
