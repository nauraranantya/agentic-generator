"""
CLI runner: batch-process generated_kg/CrewAI/*.ttl → CrewAI Python scripts.

Usage:
    From project root:
        python -m src.sparql_and_jinja2.run

    Or directly:
        python src/sparql_and_jinja2/run.py
"""

import os
import sys
import shutil

# Support both `python -m` and direct script execution
try:
    from .generator import generate_crewai
except ImportError:
    sys.path.insert(
        0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    )
    from src.sparql_and_jinja2.generator import generate_crewai


def main():
    project_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
    kg_dir = os.path.join(project_root, "generated_kg", "CrewAI")
    output_dir = os.path.join(project_root, "output_files", "output_sparql_jinja2")

    # ── Validate input ──
    if not os.path.isdir(kg_dir):
        print(f"[ERROR] KG directory not found: {kg_dir}")
        sys.exit(1)

    ttl_files = sorted(f for f in os.listdir(kg_dir) if f.endswith(".ttl"))
    if not ttl_files:
        print(f"[WARNING] No .ttl files found in {kg_dir}")
        sys.exit(0)

    # ── Clean output directory ──
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    # ── Header ──
    print("=" * 60)
    print("  SPARQL + Jinja2  →  CrewAI Code Generator")
    print("=" * 60)
    print(f"  Source : {kg_dir}")
    print(f"  Output : {output_dir}")
    print(f"  Files  : {len(ttl_files)} knowledge graphs")
    print("=" * 60)

    # ── Process each KG ──
    success = 0
    errors = []

    for filename in ttl_files:
        kg_path = os.path.join(kg_dir, filename)
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_dir, f"crewai_{base_name}.py")

        print(f"\n[Processing] {filename}")
        try:
            code = generate_crewai(kg_path, output_path)
            print(f"  → {os.path.relpath(output_path, project_root)}")
            success += 1
        except Exception as e:
            print(f"  [ERROR] {e}")
            errors.append((filename, str(e)))

    # ── Summary ──
    print("\n" + "=" * 60)
    print(f"  Done. {success}/{len(ttl_files)} files generated successfully.")
    if errors:
        print(f"  Errors ({len(errors)}):")
        for fname, err in errors:
            print(f"    - {fname}: {err}")
    print("=" * 60)


if __name__ == "__main__":
    main()
