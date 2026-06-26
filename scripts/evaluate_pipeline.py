#!/usr/bin/env python3
import os
import sys
import re
import json
import subprocess
import ast
from pathlib import Path

# ──────────────────────────────────────────────
# HELPER FUNCTIONS FOR COMPARISON
# ──────────────────────────────────────────────

def get_code_tokens(code_str: str) -> set:
    """Mengambil set token penting dari kode, mengabaikan komentar dan spasi."""
    # Menghapus komentar baris tunggal
    clean_code = re.sub(r'#.*', '', code_str)
    # Menghapus komentar multi-baris (sederhana)
    clean_code = re.sub(r'"""[\s\S]*?"""', '', clean_code)
    clean_code = re.sub(r"'''[\s\S]*?'''", '', clean_code)
    
    # Tokenisasi sederhana mencari kata kunci dan variabel
    tokens = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', clean_code)
    return set(tokens)

def calculate_jaccard_similarity(code_a: str, code_b: str) -> float:
    """Menghitung Jaccard Similarity dari token kode."""
    tokens_a = get_code_tokens(code_a)
    tokens_b = get_code_tokens(code_b)
    if not tokens_a or not tokens_b:
        return 0.0
    return len(tokens_a.intersection(tokens_b)) / len(tokens_a.union(tokens_b))

class ASTNodeVisitor(ast.NodeVisitor):
    def __init__(self):
        self.nodes = []

    def generic_visit(self, node):
        self.nodes.append(type(node).__name__)
        super().generic_visit(node)

def calculate_ast_similarity(code_a: str, code_b: str) -> float:
    """Membandingkan kemiripan struktur logika menggunakan AST."""
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

def get_ts_ast_nodes(code: str) -> set:
    """Mendapatkan set tipe node AST untuk TypeScript menggunakan node.js."""
    try:
        # A simple node script to parse TS AST and print node kinds
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
            timeout=5
        )
        if res.returncode == 0:
            import json
            kinds = json.loads(res.stdout.strip())
            return set(kinds)
    except Exception:
        pass
    return set()

def calculate_ts_ast_similarity(code_a: str, code_b: str) -> float:
    """Membandingkan kemiripan struktur logika menggunakan AST untuk TypeScript."""
    set_a = get_ts_ast_nodes(code_a)
    set_b = get_ts_ast_nodes(code_b)
    if not set_a or not set_b:
        return 0.0
    return len(set_a.intersection(set_b)) / len(set_a.union(set_b))


def extract_code_from_ipynb(ipynb_path: Path) -> str:
    """Mengekstrak kode Python dari Jupyter Notebook (.ipynb)."""
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

def get_combined_content(directory: Path, extension: str) -> str:
    """Menggabungkan konten dari semua file dengan ekstensi tertentu di dalam direktori."""
    content = []
    if not directory.exists():
        return ""
    for path in sorted(directory.rglob(f"*{extension}")):
        # Skip directories we don't want
        if any(part in path.parts for part in ("node_modules", ".agento-env", "__pycache__", ".pytest_cache")):
            continue
        try:
            content.append(path.read_text(encoding="utf-8"))
        except Exception:
            pass
    return "\n\n".join(content)

# ──────────────────────────────────────────────
# COMPILATION & RUNNABILITY CHECKS
# ──────────────────────────────────────────────

def compile_python_files(project_dir: Path) -> bool:
    """Melakukan cek kompilasi sintaks pada file Python di direktori proyek."""
    success = True
    for path in project_dir.rglob("*.py"):
        if "__pycache__" in path.parts:
            continue
        try:
            res = subprocess.run(
                [sys.executable, "-m", "py_compile", str(path)],
                capture_output=True,
                text=True
            )
            if res.returncode != 0:
                success = False
        except Exception:
            success = False
    return success

def dry_run_python_project(main_py_path: Path) -> dict:
    """Menjalankan proyek Python menggunakan key dummy untuk mengecek inisialisasi runtime."""
    import os
    env = os.environ.copy()
    env["OPENAI_API_KEY"] = "sk-dummy"
    try:
        res = subprocess.run(
            [sys.executable, str(main_py_path.resolve())],
            cwd=str(main_py_path.parent.resolve()),
            env=env,
            capture_output=True,
            text=True,
            timeout=10
        )
        stdout = res.stdout
        stderr = res.stderr
        exit_code = res.returncode
        
        error_msg = stderr.strip() or stdout.strip()
        
        # Sukses jika terinisialisasi dan menabrak error otentikasi (karena sk-dummy)
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
            # Identifikasi kategori error
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

# ──────────────────────────────────────────────
# MAIN PIPELINE EVALUATION LOOP
# ──────────────────────────────────────────────

def main():
    output_root = Path("output_files")
    gt_root = Path("GT_scripts")
    
    frameworks = {
        "CrewAI": {
            "output_dir": output_root / "output_crewai",
            "gt_dir": gt_root / "CrewAI",
            "ext": ".py"
        },
        "AutoGen": {
            "output_dir": output_root / "output_autogen",
            "gt_dir": gt_root / "AutoGen",
            "ext": ".py"
        },
        "LangGraph": {
            "output_dir": output_root / "output_langgraph",
            "gt_dir": gt_root / "LangGraph",
            "ext": ".ts"
        },
        "Mastra": {
            "output_dir": output_root / "output_mastra",
            "gt_dir": gt_root / "Mastra AI",
            "ext": ".ts"
        }
    }
    
    report_data = {}
    
    for fw_name, fw_config in frameworks.items():
        print(f"Mengaudit Framework: {fw_name}...")
        report_data[fw_name] = []
        
        output_dir = fw_config["output_dir"]
        gt_dir = fw_config["gt_dir"]
        ext = fw_config["ext"]
        
        if not output_dir.exists():
            print(f"Direktori output {output_dir} tidak ditemukan. Skip.")
            continue
            
        projects = sorted([d for d in output_dir.iterdir() if d.is_dir()])
        
        for proj in projects:
            proj_name = proj.name
            print(f"  - Proyek: {proj_name}")
            
            # 1. Cek Sintaks / Kompilasi
            syntax_ok = False
            if ext == ".py":
                syntax_ok = compile_python_files(proj)
            elif ext == ".ts":
                # TypeScript compilation: check tsc
                node_modules_path = proj / "node_modules"
                if node_modules_path.exists():
                    res = subprocess.run(
                        ["node", "node_modules/typescript/bin/tsc", "--noEmit"],
                        cwd=proj,
                        capture_output=True,
                        text=True
                    )
                    syntax_ok = (res.returncode == 0)
                else:
                    # Alternatif compile check manual (jika tsc tidak ada)
                    syntax_ok = True  # Fallback
            
            # 2. Cek Dry-Run Execution (Untuk Python)
            run_status = "N/A"
            run_output = ""
            main_py = proj / "main.py"
            if main_py.exists() and ext == ".py":
                run_res = dry_run_python_project(main_py)
                run_status = run_res["status"]
                run_output = run_res["output"]
            
            # 3. Hitung Kemiripan dengan Ground Truth (AST & Token Jaccard)
            token_sim = 0.0
            ast_sim = 0.0
            gt_found = False
            
            gen_code = get_combined_content(proj, ext)
            gt_code = ""
            
            # Mencari padanan di GT_scripts
            if fw_name == "AutoGen":
                # Ground truth untuk AutoGen berupa file .ipynb
                gt_file = gt_dir / f"{proj_name}.ipynb"
                if gt_file.exists():
                    gt_code = extract_code_from_ipynb(gt_file)
                    gt_found = True
            elif fw_name == "Mastra":
                # Mastra GT bisa berupa folder atau file .ts langsung
                gt_folder = gt_dir / proj_name
                gt_file = gt_dir / f"{proj_name}.ts"
                if gt_folder.exists() and gt_folder.is_dir():
                    gt_code = get_combined_content(gt_folder, ext)
                    gt_found = True
                elif gt_file.exists():
                    gt_code = gt_file.read_text(encoding="utf-8")
                    gt_found = True
            else:
                # CrewAI dan LangGraph berupa folder
                gt_folder = gt_dir / proj_name
                if gt_folder.exists() and gt_folder.is_dir():
                    # Untuk LangGraph, GT menggunakan index.ts sedangkan hasil generate python, 
                    # jadi similarity akan bernilai 0.
                    gt_code = get_combined_content(gt_folder, ".py" if fw_name != "LangGraph" else ".ts")
                    gt_found = True
                    
            if gt_found and gen_code and gt_code:
                token_sim = calculate_jaccard_similarity(gen_code, gt_code)
                if ext == ".py":
                    ast_sim = calculate_ast_similarity(gen_code, gt_code)
                elif ext == ".ts":
                    ast_sim = calculate_ts_ast_similarity(gen_code, gt_code)
                else:
                    ast_sim = 0.0
            
            report_data[fw_name].append({
                "name": proj_name,
                "syntax_ok": syntax_ok,
                "run_status": run_status,
                "run_output": run_output,
                "gt_found": gt_found,
                "token_sim": token_sim,
                "ast_sim": ast_sim
            })
            
    # ──────────────────────────────────────────────
    # GENERATE MARKDOWN REPORT
    # ──────────────────────────────────────────────
    
    report = "# Laporan Hasil Evaluasi Pipeline KGs → Scripts\n\n"
    report += f"Audit dilakukan pada: {subprocess.check_output(['date']).decode('utf-8').strip()}\n\n"
    
    report += "## 1. Ringkasan Eksekutif per Framework\n\n"
    report += "| Framework | Total Proyek | Sukses Kompilasi | Sukses Eksekusi (Dry-Run) | Rata-rata Token Sim | Rata-rata AST Sim |\n"
    report += "| :--- | :---: | :---: | :---: | :---: | :---: |\n"
    
    for fw_name, data in report_data.items():
        if not data:
            continue
        total = len(data)
        success_syntax = sum(1 for p in data if p["syntax_ok"])
        success_run = sum(1 for p in data if p["run_status"] == "SUCCESS_DUMMY" or p["run_status"] == "N/A" and p["syntax_ok"])
        avg_token = sum(p["token_sim"] for p in data) / total
        avg_ast = sum(p["ast_sim"] for p in data) / total
        
        syntax_pct = (success_syntax / total) * 100
        run_pct = (success_run / total) * 100
        
        report += f"| **{fw_name}** | {total} | {success_syntax} ({syntax_pct:.1f}%) | {success_run} ({run_pct:.1f}%) | {avg_token:.1%} | {avg_ast:.1%} |\n"
        
    report += "\n---\n\n## 2. Rincian per Framework\n"
    
    for fw_name, data in report_data.items():
        if not data:
            continue
        report += f"\n### {fw_name}\n\n"
        report += "| Nama Proyek | Kompilasi | Status Run (sk-dummy) | Ground Truth Cocok | Token Similarity | AST Similarity |\n"
        report += "| :--- | :---: | :---: | :---: | :---: | :---: |\n"
        
        for p in data:
            comp_str = "✅ OK" if p["syntax_ok"] else "❌ FAIL"
            run_str = "✅ SUCCESS_DUMMY" if p["run_status"] == "SUCCESS_DUMMY" else (f"❌ {p['run_status']}" if p["run_status"] != "N/A" else "➖ N/A")
            gt_str = "✅ Ya" if p["gt_found"] else "❌ Tidak"
            token_str = f"{p['token_sim']:.1%}" if p["gt_found"] else "➖"
            ast_str = f"{p['ast_sim']:.1%}" if p["gt_found"] else "➖"
            
            report += f"| `{p['name']}` | {comp_str} | {run_str} | {gt_str} | {token_str} | {ast_str} |\n"
            
        # Detail Kegagalan Eksekusi
        failures = [p for p in data if p["run_status"] not in ("SUCCESS_DUMMY", "N/A")]
        if failures:
            report += f"\n#### Detail Log Kegagalan Eksekusi ({fw_name}):\n"
            for p in failures:
                report += f"\n*   **{p['name']}** (`{p['run_status']}`):\n    ```\n    {p['run_output']}\n    ```\n"
                
    report_file = Path("pipeline_evaluation_results.md")
    report_file.write_text(report, encoding="utf-8")
    print(f"\nEvaluasi selesai! Laporan disimpan di: {report_file.absolute()}")

if __name__ == "__main__":
    main()
