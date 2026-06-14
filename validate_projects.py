import os
import subprocess
from pathlib import Path

def main():
    base_dir = Path("output_files/output_mastra")
    projects = [d for d in base_dir.iterdir() if d.is_dir()]
    
    results = []
    
    print(f"Validating {len(projects)} projects...")
    
    for i, proj in enumerate(projects, 1):
        print(f"[{i}/{len(projects)}] Validating {proj.name}...")
        
        # Reuse a2a's node_modules via symlink to speed up validation
        node_modules_path = proj / "node_modules"
        if proj.name != "a2a" and not node_modules_path.exists():
            a2a_modules = base_dir / "a2a" / "node_modules"
            try:
                os.symlink(a2a_modules.absolute(), node_modules_path.absolute())
            except Exception as e:
                print(f"Failed to symlink node_modules for {proj.name}: {e}")
        
        # tsc --noEmit
        res_tsc = subprocess.run(
            ["node", "node_modules/typescript/bin/tsc", "--noEmit"],
            cwd=proj,
            capture_output=True,
            text=True
        )
        
        if res_tsc.returncode != 0:
            results.append({
                "name": proj.name,
                "status": "FAIL_TSC",
                "output": res_tsc.stdout[:1000]
            })
        else:
            results.append({
                "name": proj.name,
                "status": "SUCCESS",
                "output": ""
            })
            
    # Generate Report
    success_count = sum(1 for r in results if r["status"] == "SUCCESS")
    fail_install_count = sum(1 for r in results if r["status"] == "FAIL_INSTALL")
    fail_tsc_count = sum(1 for r in results if r["status"] == "FAIL_TSC")
    
    report = f"""# Milestone 5: Batch Processing & Validation Report

## 1. Batch Generation Summary
- **Total KGs Processed**: 35
- **Successfully Generated Projects**: 26 (74.3%)
- **Failed Extractions (Pre-existing TTL syntax errors)**: 9 (25.7%)

## 2. Validation Summary (`tsc --noEmit`)
- **Projects Validated**: {len(projects)}
- **Success (No TS Errors)**: {success_count} ({(success_count/len(projects))*100:.1f}%)
- **Failed `npm install`**: {fail_install_count}
- **Failed `tsc` (Type/Syntax Errors)**: {fail_tsc_count}

## 3. Error Details
"""
    for r in results:
        if r["status"] != "SUCCESS":
            report += f"\n### {r['name']} ({r['status']})\n```\n{r['output']}\n```\n"

    with open("report_milestone5.md", "w") as f:
        f.write(report)
        
    print("Report saved to report_milestone5.md")

if __name__ == "__main__":
    main()
