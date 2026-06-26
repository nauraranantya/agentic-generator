"""
CLI Runner: batch-process kgs_original/Mastra AI/*.ttl → TypeScript Mastra projects

Pipeline: KG (.ttl) → agnostic extraction → Mastra adapter → TypeScript generation

Usage:
    From project root:
        python -m src.frameworks.mastra.run

    Single file:
        python -m src.frameworks.mastra.run path/to/file.ttl

    Or directly:
        python src/mastra/run.py
"""

import os
import sys
import shutil
from pathlib import Path

# Support both `python -m` and direct script execution
try:
    from ...core.extractor import extract_project
    from .adapter import adapt
    from .generator import generate_project
except ImportError:
    sys.path.insert(
        0, str(Path(__file__).parent.parent.parent.parent)
    )
    from src.core.extractor import extract_project
    from src.frameworks.mastra.adapter import adapt
    from src.frameworks.mastra.generator import generate_project


def process_single(kg_path: str, output_dir: str) -> str:
    """
    Process a single TTL file through the 3-layer pipeline.

    Args:
        kg_path:    Path to the input .ttl file
        output_dir: Directory to write the generated project

    Returns:
        The output directory path
    """
    print(f"\n{'=' * 65}")
    print(f"  Processing: {Path(kg_path).name}")
    print(f"{'=' * 65}")
    
    try:
        # Layer 1 + Layer 2: agnostic extraction -> Mastra-specific adaptation
        print("  [1/3] KG extraction + Mastra adaptation...")
        project = adapt(extract_project(kg_path))
        
        # Override project_var_name with the filename to prevent overwriting
        base_name = Path(kg_path).stem
        dir_name = base_name.replace("_instances", "")
        project.project_var_name = dir_name
        
        print(f"  ✓ Extracted: {len(project.agents)} agents, "
              f"{len(project.tools)} tools, {len(project.workflows)} workflows")
        
        # Layer 3: File generation (TypeScript + Jinja2)
        print("  [2/3] TypeScript code generation...")
        output_path = generate_project(project, output_dir)
        
        print(f"  ✓ Generated: {output_path}")
        
        # Summary
        print("  [3/3] Summary:")
        print(f"    - Project: {project.project_name}")
        print(f"    - Agents: {len(project.agents)}")
        print(f"    - Tools: {len(project.tools)}")
        print(f"    - Workflows: {len(project.workflows)}")
        print(f"    - Output: {output_path}")
        print(f"{'=' * 65}\n")
        
        return output_path
        
    except Exception as e:
        print(f"  ✗ ERROR: {str(e)}")
        print(f"{'=' * 65}\n")
        raise


def main():
    """Main CLI entry point."""
    project_root = Path(__file__).parent.parent.parent.parent
    output_base = project_root / "output_files" / "output_mastra"

    # ── Handle single-file mode ──
    if len(sys.argv) > 1 and sys.argv[1].endswith(".ttl"):
        kg_path = Path(sys.argv[1]).resolve()
        
        if not kg_path.exists():
            print(f"[ERROR] File not found: {kg_path}")
            sys.exit(1)
        
        base_name = kg_path.stem
        # Remove _instances suffix for cleaner directory name
        dir_name = base_name.replace("_instances", "")
        output_dir = output_base / dir_name

        print(f"\n{'=' * 65}")
        print(f"  Mastra AI Code Generator - Single File Mode")
        print(f"{'=' * 65}")
        print(f"  Input : {kg_path}")
        print(f"  Output: {output_dir}")
        print(f"{'=' * 65}")
        
        process_single(str(kg_path), str(output_base))
        
        print(f"\n✓ Done! TypeScript project generated at:")
        print(f"  {output_dir}")
        print(f"\nNext steps:")
        print(f"  cd {output_dir}")
        print(f"  npm install")
        print(f"  npm run dev")
        return

    # ── Batch mode: process all TTL files ──
    kg_dir = project_root / "kgs_original" / "Mastra AI"

    if not kg_dir.is_dir():
        print(f"[ERROR] KG directory not found: {kg_dir}")
        sys.exit(1)

    ttl_files = sorted([f for f in kg_dir.iterdir() if f.suffix == ".ttl"])
    
    if not ttl_files:
        print(f"[WARNING] No .ttl files found in {kg_dir}")
        sys.exit(0)

    # Clean output directory (commented out to preserve node_modules caches)
    # if output_base.exists():
    #     print(f"[INFO] Cleaning output directory: {output_base}")
    #     shutil.rmtree(output_base)
    output_base.mkdir(parents=True, exist_ok=True)

    # Header
    print("\n")
    print("=" * 65)
    print("  Mastra AI Code Generator - Batch Mode")
    print("  Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript")
    print("=" * 65)
    print(f"  Source : {kg_dir}")
    print(f"  Output : {output_base}")
    print(f"  Files  : {len(ttl_files)} knowledge graphs")
    print("=" * 65)
    print()

    # Process each KG
    success = 0
    errors = []
    
    for i, ttl_file in enumerate(ttl_files, 1):
        print(f"[{i}/{len(ttl_files)}] {ttl_file.name}")
        
        try:
            process_single(str(ttl_file), str(output_base))
            success += 1
        except Exception as e:
            error_msg = f"{ttl_file.name}: {str(e)}"
            errors.append(error_msg)
            print(f"  ✗ FAILED: {error_msg}\n")
            continue

    # Final summary
    print("\n")
    print("=" * 65)
    print("  Batch Processing Complete")
    print("=" * 65)
    print(f"  Total    : {len(ttl_files)} files")
    print(f"  Success  : {success} projects generated")
    print(f"  Failed   : {len(errors)} errors")
    print("=" * 65)
    
    if errors:
        print("\n  Errors:")
        for err in errors:
            print(f"    - {err}")
    
    print(f"\n  Output directory: {output_base}")
    print("=" * 65)
    print()


if __name__ == "__main__":
    main()
