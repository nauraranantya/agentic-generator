# Agento — Knowledge-Graph-to-Code Generation for Agentic AI Frameworks

Agento is a research pipeline that transforms Knowledge Graphs (KGs) describing agentic AI systems into executable, framework-native source code. KGs are authored against the [Agentic AI Ontology](https://w3id.org/agentic-ai/onto) and compiled into runnable projects for **CrewAI**, **AutoGen**, **LangGraph**, and **Mastra**.

The project's purpose is to evaluate whether a single, framework-agnostic semantic representation can be losslessly and faithfully re-materialized as idiomatic code across heterogeneous multi-agent frameworks — and to quantify that fidelity empirically against ground-truth reference implementations.

---

## Architecture

The pipeline is organized as a strict, unidirectional 3-layer conversion process:

```
  .ttl / .rdf KG                     Canonical IR                Framework Project
 (kgs_original/)                   (Pydantic models)              (output_files/)
        │                                 │                             │
        ▼                                 ▼                             ▼
 ┌──────────────┐   SPARQL   ┌────────────────────────┐  adapt   ┌──────────────┐  generate  ┌───────────────┐
 │  RDF Graph   │ ─────────► │   Framework-agnostic    │ ───────► │  Framework-   │ ─────────► │ Python / TS   │
 │  (rdflib)    │  extractor │   Intermediate          │  adapter │  specific IR  │ generator  │ project files │
 └──────────────┘            │   Representation (IR)  │          └──────────────┘             └───────────────┘
                              └────────────────────────┘
```

1. **Extraction (`src/core/extractor.py`, `src/core/queries.py`)** — Loads a `.ttl`/`.rdf` graph with `rdflib` and runs SPARQL queries against the Agentic AI Ontology schema to pull out agents, tasks, tools, workflows, goals, resources, constraints, and configuration.
2. **Canonical IR (`src/core/models.py`)** — Extracted triples are normalized into a framework-agnostic Pydantic model tree. This IR is the single contract shared by every downstream framework; it contains no framework-specific vocabulary.
3. **Adaptation (`src/frameworks/<framework>/adapter.py`)** — Maps the canonical IR onto a framework-specific IR (e.g. Crew/Agent/Task for CrewAI, StateGraph/Node/Edge for LangGraph).
4. **Generation (`src/frameworks/<framework>/generator.py`)** — Renders the framework-specific IR into runnable project files (Python modules, YAML configs, or TypeScript for Mastra) via Jinja2 templates.

Each framework has its own independent adapter/generator pair; there is no shared rendering abstraction across frameworks — only the canonical IR is shared.

---

## Repository Layout

```
src/
├── core/                    # Framework-agnostic extraction & canonical IR (shared by all frameworks)
│   ├── extractor.py         # rdflib loading + SPARQL-driven extraction
│   ├── queries.py           # SPARQL query definitions
│   ├── models.py            # Canonical IR (Pydantic)
│   ├── normalizer.py        # IR normalization helpers
│   └── helpers.py
│
├── frameworks/
│   ├── crewai/              # adapter.py, generator.py, models.py, run.py
│   ├── autogen/             # adapter.py, generator.py, models.py, run.py
│   ├── langgraph/           # adapter.py, generator.py, models.py, run.py
│   └── mastra/              # adapter.py, generator.py, extractor.py, models.py, run.py
│
└── evaluation/              # OEC / WGI fidelity evaluation suite (see src/evaluation/README.md)
    ├── run.py                # Per-framework generation-vs-KG evaluation
    ├── interop_run.py        # Cross-framework interoperability evaluation
    ├── metrics/              # AST similarity, compilation checks, dry-run, OEC, WGI
    └── extractors/

kgs_original/                # Input KGs (.ttl), one subfolder per framework
├── CrewAI/
├── AutoGen/
├── LangGraph/
└── Mastra AI/

GT_scripts/                  # Ground-truth reference implementations (DO NOT EDIT)
├── CrewAI/
├── AutoGen/
├── LangGraph/
└── Mastra AI/

output_files/                 # Generated output (regenerated on each run, can be stale)
├── output_crewai/
├── output_autogen/
├── output_langgraph/
├── output_mastra/
└── output_interop/

tests/                        # Unit tests for extractor and adapters
evaluation_results/            # Evaluation reports (JSON + Markdown)
```

---

## Installation

Requires Python 3.10–3.13.

```bash
git clone https://github.com/raviearjun/agentic-generator-paper.git
cd agentic-generator-paper
python -m venv venv
source venv/bin/activate      # macOS/Linux
pip install -e .
```

Dependencies (`rdflib`, `pydantic`, `crewai`, `autogen-agentchat`, `python-dotenv`, etc.) are declared in `pyproject.toml`.

---

## Usage

### Generate code for a framework

Batch-process every KG under `kgs_original/<Framework>/` and emit projects into `output_files/output_<framework>/`:

```bash
python -m src.frameworks.crewai.run
python -m src.frameworks.autogen.run
python -m src.frameworks.langgraph.run
python -m src.frameworks.mastra.run
```

To process a single KG file instead of the full batch:

```bash
python -m src.frameworks.crewai.run kgs_original/CrewAI/job-posting_instances.ttl
```

### Validate against ground truth

Compare generated output in `output_files/output_<framework>/<project>/` with the corresponding reference implementation in `GT_scripts/<Framework>/<project>/`.

### Run the evaluation suite

Quantitative fidelity metrics (Ontology Element Coverage and Workflow Graph Isomorphism) between the source KG and generated code:

```bash
python -m src.evaluation.run
python -m src.evaluation.run --framework crewai   # or autogen / langgraph / mastra
```

Cross-framework interoperability scoring:

```bash
python -m src.evaluation.interop_run
```

Results are written to `evaluation_results/` as `oec_wgi_results.json` and `oec_wgi_results.md`. See `src/evaluation/README.md` for metric definitions.

### Run tests

```bash
pytest tests/
```

---

## Development Workflow

1. Modify extraction/IR logic in `src/core/`, or adapter/generator logic in `src/frameworks/<framework>/`.
2. Re-run the corresponding `python -m src.frameworks.<framework>.run`.
3. Diff generated output in `output_files/` against `GT_scripts/`.
4. Re-run `python -m src.evaluation.run` to confirm fidelity metrics have not regressed.

Editing rules:
- Only modify files under `src/`.
- Never hand-edit `output_files/` (regenerated) or `GT_scripts/` (reference, read-only).
- Changes to `src/core/` affect all four frameworks — validate against every framework's ground truth after any core change.
- Framework adapter/generator pairs are independent; a schema change typically requires updating all four.

See `AGENTS.md` for the full contributor/agent reference guide.

---

## Ontology

KGs are expressed in RDF/Turtle against the [Agentic AI Ontology](https://w3id.org/agentic-ai/onto), which models agents, tasks, tools, workflows, goals, capabilities, resources, constraints, and configuration as first-class ontology classes. The canonical IR in `src/core/models.py` maps one-to-one onto this schema, independent of any target framework's vocabulary.

## License

No license file is currently published in this repository.
