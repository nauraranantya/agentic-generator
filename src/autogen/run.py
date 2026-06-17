"""
CLI Runner: batch-process generated_kg/AutoGen/*.ttl → AutoGen project directories.

Pipeline: KG (.ttl) → agnostic extraction → AutoGen adapter → code generation.
"""

import os
import shutil
import sys

try:
    from ..core.extractor import extract_project
    from .adapter import adapt
    from .generator import generate_project
except ImportError:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
    from src.core.extractor import extract_project
    from src.autogen.adapter import adapt
    from src.autogen.generator import generate_project


def process_single(kg_path: str, output_dir: str) -> str:
    project = adapt(extract_project(kg_path))
    return generate_project(project, output_dir)


def main() -> None:
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    kg_dir = os.path.join(project_root, "generated_kg", "AutoGen")
    output_base = os.path.join(project_root, "output_files", "output_autogen")

    if len(sys.argv) > 1 and sys.argv[1].endswith(".ttl"):
        kg_path = os.path.abspath(sys.argv[1])
        base_name = os.path.splitext(os.path.basename(kg_path))[0]
        output_dir = os.path.join(output_base, base_name.replace("_instances", ""))
        print(f"[Processing] {kg_path}")
        process_single(kg_path, output_dir)
        print(f"[Done] -> {output_dir}")
        return

    if not os.path.isdir(kg_dir):
        print(f"[ERROR] KG directory not found: {kg_dir}")
        sys.exit(1)

    ttl_files = sorted(f for f in os.listdir(kg_dir) if f.endswith(".ttl"))
    if not ttl_files:
        print(f"[WARNING] No .ttl files found in {kg_dir}")
        return

    if os.path.exists(output_base):
        shutil.rmtree(output_base)
    os.makedirs(output_base, exist_ok=True)

    success = 0
    failures = []
    for filename in ttl_files:
        kg_path = os.path.join(kg_dir, filename)
        output_dir = os.path.join(output_base, os.path.splitext(filename)[0].replace("_instances", ""))
        print(f"[Processing] {filename}")
        try:
            process_single(kg_path, output_dir)
            success += 1
        except Exception as exc:
            failures.append((filename, str(exc)))
            print(f"  [ERROR] {exc}")

    print(f"[Done] {success}/{len(ttl_files)} generated")
    if failures:
        for name, error in failures:
            print(f"  - {name}: {error}")


if __name__ == "__main__":
    main()
