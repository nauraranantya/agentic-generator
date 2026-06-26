"""CLI for OEC/WGI evaluation of KG-to-framework generated outputs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, Iterable, List

from .config import framework_configs
from .extractors.code_extractor import extract_code
from .extractors.kg_extractor import extract_kg
from .metrics.oec import calculate_oec
from .metrics.wgi import calculate_wgi
from .pairing import pair_projects
from .reports.markdown_report import render_markdown


def main() -> None:
    args = _parse_args()
    root = args.root.resolve()
    configs = framework_configs(root)

    selected = [args.framework] if args.framework != "all" else list(configs.keys())
    results = {"root": str(root), "frameworks": []}

    for key in selected:
        config = configs[key]
        framework_result = _evaluate_framework(key, config)
        results["frameworks"].append(framework_result)

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "oec_wgi_results.json"
    md_path = output_dir / "oec_wgi_results.md"
    json_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    md_path.write_text(render_markdown(results), encoding="utf-8")

    print(f"Evaluation written to {json_path}")
    print(f"Report written to {md_path}")


def _evaluate_framework(key: str, config) -> Dict[str, object]:
    projects = []
    for kg_path, project_dir, project_name in pair_projects(config):
        print(f"[{config.name}] {project_name}")
        if not project_dir.exists():
            projects.append(
                {
                    "project": project_name,
                    "kg_path": str(kg_path),
                    "output_dir": str(project_dir),
                    "status": "missing_output",
                    "error": f"Generated output directory not found: {project_dir}",
                }
            )
            continue
        try:
            kg = extract_kg(kg_path)
            code = extract_code(project_dir, key)
            oec = calculate_oec(kg, code)
            wgi = calculate_wgi(kg, code)
            projects.append(
                {
                    "project": project_name,
                    "kg_path": str(kg_path),
                    "output_dir": str(project_dir),
                    "status": "ok",
                    "kg_element_count": len(kg.elements),
                    "code_element_count": len(code.elements),
                    "oec": oec,
                    "wgi": wgi,
                }
            )
        except Exception as exc:
            projects.append(
                {
                    "project": project_name,
                    "kg_path": str(kg_path),
                    "output_dir": str(project_dir),
                    "status": "error",
                    "error": str(exc),
                }
            )

    return {
        "key": key,
        "name": config.name,
        "kg_dir": str(config.kg_dir),
        "output_dir": str(config.output_dir),
        "summary": _summary(projects),
        "projects": projects,
    }


def _summary(projects: List[Dict[str, object]]) -> Dict[str, object]:
    ok_projects = [project for project in projects if project.get("status") == "ok"]
    errors = len(projects) - len(ok_projects)
    return {
        "projects": len(projects),
        "evaluated": len(ok_projects),
        "errors": errors,
        "avg_oec_all": _avg(project["oec"]["all_extracted"]["score"] for project in ok_projects),
        "avg_oec_important": _avg(project["oec"]["important_subset"]["score"] for project in ok_projects),
        "avg_wgi": _avg(project["wgi"]["score"] for project in ok_projects),
        "avg_edge_f1": _avg(project["wgi"]["edge_f1"] for project in ok_projects),
    }


def _avg(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate KG-to-framework conversion with OEC and WGI.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Repository root containing kgs_original/ and output_files/.",
    )
    parser.add_argument(
        "--framework",
        choices=["all", "crewai", "autogen", "langgraph", "mastra"],
        default="all",
        help="Framework to evaluate.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("evaluation_results"),
        help="Directory for JSON and Markdown evaluation reports.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main()
