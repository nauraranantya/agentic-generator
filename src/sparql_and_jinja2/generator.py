"""
Generator: orchestrates SPARQL extraction + Jinja2 rendering.

Public API:
    generate_crewai(kg_path, output_path) -> str
"""

import os
from typing import Optional

from jinja2 import Environment, FileSystemLoader

from .extractor import extract_all


# ──────────────────────────────────────────────
# Custom Jinja2 filter
# ──────────────────────────────────────────────

def _python_string(s: str) -> str:
    """
    Render a value as a Python string literal.

    - Empty / None  → ''
    - Single-line   → repr()        e.g. 'hello world'
    - Multi-line    → triple-quoted  e.g. \"\"\"line1\\nline2\"\"\"
    """
    if not s:
        return "''"
    s = s.strip()
    if "\n" in s or len(s) > 120:
        # Triple-quoted string for readability
        escaped = s.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
        return f'"""{escaped}"""'
    return repr(s)


# ──────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────

def generate_crewai(kg_path: str, output_path: str) -> str:
    """
    Full declarative pipeline:
        KG (.ttl) → SPARQL extraction → Jinja2 template → .py output

    Args:
        kg_path:     Path to the input Knowledge Graph file (.ttl / .rdf)
        output_path: Path to write the generated CrewAI Python script

    Returns:
        The generated Python source code as a string
    """
    # 1. Extract structured data via SPARQL
    data = extract_all(kg_path)

    # 2. Setup Jinja2 environment
    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(
        loader=FileSystemLoader(template_dir),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    env.filters["pystr"] = _python_string

    template = env.get_template("crewai.py.j2")

    # 3. Render template with extracted data
    code = template.render(**data)

    # 4. Write output file
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(code)

    return code
