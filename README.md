# Agento: Cross-Framework Code Generation as Proof-of-Concept Validation for the AgentO Ontology

[![Ontology](https://img.shields.io/badge/Ontology-AgentO-blue.svg)](https://w3id.org/agentic-ai/onto)
[![Paper](https://img.shields.io/badge/Paper-ESWC%202025-red.svg)](_ESWC25__Ontology_for_Agentic_AI_Systems.pdf)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18342624-blue.svg)](https://doi.org/10.5281/zenodo.18342624)
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-green.svg)](https://www.python.org/)
[![SPARQL](https://img.shields.io/badge/SPARQL-Endpoint-orange.svg)](https://w3id.org/agentic-ai/sparql)

This repository implements an extension of the following peer-reviewed publication:

> **AgentO: An Ontology for Modeling Agentic AI Systems**
> *Extended Semantic Web Conference (ESWC 2025)*
> Andreas Ekelhart<sup>1,2</sup>, Kabul Kurniawan<sup>3</sup>, Fajar J. Ekaputra<sup>4</sup>, Elmar Kiesling<sup>4</sup>
>
> <sup>1</sup>University of Vienna, Austria &nbsp;&nbsp; <sup>2</sup>SBA Research, Vienna, Austria &nbsp;&nbsp; <sup>3</sup>Universitas Gadjah Mada, Indonesia &nbsp;&nbsp; <sup>4</sup>Vienna University of Economics and Business, Austria

---

## Overview

Agentic AI systems — characterized by autonomy, goal-directed behavior, and multi-step workflow orchestration — are increasingly deployed across diverse domains including cybersecurity, finance, healthcare, and scientific research. Despite widespread adoption, current implementations across frameworks such as AutoGen, CrewAI, LangGraph, and Mastra AI typically encode logic and workflows directly in code, resulting in ad-hoc, monolithic software architectures that hinder scalability, reusability, and interoperability.

The base paper introduced **AgentO** (Agentic AI Ontology), an OWL/RDF-based ontology providing a standardized vocabulary for formally modeling the core components of agentic patterns — including agents, tasks, goals, tools, resources, workflow patterns, and their interrelations. The ontology was used to construct a Knowledge Graph (KG) by translating 66 agentic workflows from four heterogeneous frameworks, and validated through three real-world use cases: declarative pattern reconstruction, cross-context component reuse, and agentic workflow auditing.

**This project extends the original research** by implementing a bidirectional compilation pipeline to demonstrate that AgentO constitutes a *generatively valid*, framework-agnostic intermediate representation (IR). Concretely, we validate the ontology's semantic completeness by:

1. **Ontology Population (`script_to_kg`)**: LLM-driven extraction of AgentO-compliant RDF triples from reference framework source code.
2. **Ontology Materialization (`kg_to_script`)**: Deterministic compilation of AgentO KG instances into fully executable, native multi-agent workflows across target frameworks.
3. **Execution Validation**: Automated functional verification (syntax compilation, dry-run execution, fidelity metrics) to confirm that the ontology captures sufficient execution semantics for end-to-end workflow reconstruction.

---

## Research Contribution

The central thesis of this extension is as follows: if an agentic workflow instantiated from framework *A* can be faithfully represented in AgentO, and subsequently compiled into a functionally correct, executable implementation for framework *B* — without loss of critical orchestration semantics (agent roles, task assignments, tool bindings, prompt instructions, workflow topology) — then AgentO is empirically validated as a semantically complete, framework-agnostic vocabulary.

This provides two complementary validation dimensions:

- **Semantic Completeness**: Cross-framework translation preserves agent roles, task structures, tool assignments, prompt content, and workflow patterns (sequential, parallel, nested), demonstrating that the ontology's class and property hierarchy is sufficiently expressive.
- **Execution Fidelity**: Generated scripts must not merely be syntactically correct; they must execute successfully, confirming that the ontology captures the runtime orchestration semantics necessary to construct functional agentic software.

---

## Ontology Summary

AgentO is formalized as an OWL/RDF ontology reusing concepts from PROV-O (`prov:Agent`), P-Plan (`pplan:Plan`, `pplan:Step`), and BEAM (`beam:System`, `beam:Context`, `beam:Resource`). The ontology defines 23 core classes and 40+ object/data properties covering:

| Core Class | Description |
|---|---|
| `LLMAgent` | Autonomous AI agent backed by a language model |
| `HumanAgent` | Human participant collaborating within a workflow |
| `Task` | Discrete activity contributing to an objective |
| `WorkflowPattern` | Reusable structured workflow template (Sequential / Parallel / Nested) |
| `WorkflowStep` | Individual action or phase within a workflow pattern |
| `Tool` | Instrument extending agent capabilities (APIs, search, databases) |
| `Resource` | Asset consumed or produced by agents or tasks |
| `Goal` | Desired state an agent or team aims to achieve |
| `Objective` | Collective target assigned to a team |
| `Team` | Coordinated group of LLM agents |
| `Prompt` | Structured instruction or input given to an agent |
| `KnowledgeBase` | Structured information store referenced by agents |
| `Memory` | Persistent state supporting agent reasoning across steps |
| `LanguageModel` | Underlying model powering LLM agents |

Full ontology specification: [https://w3id.org/agentic-ai/onto](https://w3id.org/agentic-ai/onto)  
SPARQL endpoint: [https://w3id.org/agentic-ai/sparql](https://w3id.org/agentic-ai/sparql)

---

## System Architecture

The workspace comprises two decoupled, independently installable pipelines. Communication between pipelines is strictly mediated through AgentO RDF Turtle (`.ttl`) files on disk.

```
┌──────────────────────────────────────┐
│   Ground Truth Reference Scripts     │  ◄──┐
│  (AutoGen, CrewAI, LangGraph,        │     │
│   Mastra AI) — 66 agentic workflows  │     │
└──────────────────┬───────────────────┘     │
                   │                          │
    [script_to_kg] │ LLM-driven extraction    │ [kg_to_script]
                   ▼                          │ Deterministic compilation
┌──────────────────────────────────────┐      │
│   AgentO Knowledge Graph (.ttl)      │ ─────┘
│   RDF Turtle — AgentO schema         │
└──────────────────┬───────────────────┘
                   │
                   │ Automated evaluation suite
                   ▼
┌──────────────────────────────────────┐
│   Validation Suite                   │
│   - Syntax compilation               │
│   - Dry-run execution                │
│   - Ontology Element Coverage (OEC)  │
│   - Workflow Graph Isomorphism (WGI) │
│   - AST structural similarity        │
└──────────────────────────────────────┘
```

### Pipeline 1: Script-to-KG (`script_to_kg/`)

**Role**: Ontology population — automated extraction of AgentO-compliant KG instances from framework source code.

**Process**:
1. Loads reference ground-truth source code from `ground_truth_scripts/<Framework>/`.
2. Constructs a prompt from a variant template (`prompts/<variant>.md`) concatenated with the ontology schema (`agentO.ttl`) and source code.
3. Invokes an LLM backend (OpenAI / Gemini / Anthropic) to perform semantic mapping and produce RDF triples conforming to the AgentO schema.
4. Serializes output KG instances to `generated_kgs/<Framework>/<PromptID>/<Model>/*.ttl`.

The pipeline processed approximately 2.8M input tokens and 570K output tokens to translate the 66 reference patterns into AgentO.

**Source patterns by framework**: AutoGen (6), CrewAI (16), LangGraph (9), Mastra AI (35)

### Pipeline 2: KG-to-Script (`kg_to_script/`)

**Role**: Ontology materialization — deterministic translation of AgentO KG instances into executable framework-native code.

**Process**:
1. **Extraction** (`core/extractor.py`): Loads `.ttl` graphs via `rdflib` and executes SPARQL queries bound to the AgentO schema to retrieve typed entity relationships.
2. **Canonical IR** (`core/models.py`): Normalizes SPARQL query results into framework-agnostic Pydantic models representing agents, tasks, workflows, tools, prompts, and resources.
3. **Framework Adaptation** (`frameworks/<framework>/adapter.py`): Maps canonical IR onto framework-specific IR, resolving framework idioms (e.g., CrewAI `Crew`, AutoGen `GroupChat`, LangGraph state machine edges, Mastra workflow steps).
4. **Code Generation** (`frameworks/<framework>/generator.py`): Renders framework-specific IR to executable Python or TypeScript scripts in `generated_projects/`.

---

## Knowledge Graph — Source Patterns

The base KG was constructed from 66 reference agentic workflow templates sourced from official framework repositories, spanning workflow patterns across diverse application domains (travel planning, financial analysis, recruitment, stock analysis, marketing, software development, and others).

The three primary workflow patterns modeled in AgentO are:

| Pattern | Description |
|---|---|
| **Sequential** | Tasks executed linearly; output of one agent serves as input to the next |
| **Parallel** | Multiple agents execute concurrently on independent sub-tasks; results are aggregated |
| **Nested** | Sub-workflows (themselves sequential, parallel, or nested) are invoked within a parent workflow |

---

## Evaluation Suite

Generative validity of the ontology is assessed through an automated five-metric evaluation suite:

| Metric | Description |
|---|---|
| **Syntax Verification** | Python/TypeScript compilation check; confirms absence of indentation, import, and syntax errors |
| **Functional Dry-Run** | Executes generated entry points with dummy API credentials; a clean exit or expected authentication error (no `ImportError`, `NameError`, `TypeError`) confirms correct structural instantiation |
| **Ontology Element Coverage (OEC)** | Percentage of ontology classes and object properties populated in the source KG that are correctly materialized in the generated code |
| **Workflow Graph Isomorphism (WGI)** | Structural alignment score between the multi-agent communication topology encoded in the source KG and the topology recovered from the generated code |
| **AST Structural Similarity** | Measures syntactic alignment of generated code against ground-truth reference implementations |

---

## Repository Layout

```
.
├── agentO.ttl                            # AgentO ontology definition (OWL/RDF)
├── _ESWC25__Ontology_for_Agentic_AI_Systems.pdf  # Base research paper (ESWC 2025)
├── legacy_reports/                       # Historical evaluation reports (reference only)
│
├── script_to_kg/                         # Pipeline 1: Script → KG
│   ├── src/
│   │   ├── run_experiment.py             # Multi-prompt, multi-model KG generation runner
│   │   └── run_all_experiments.sh
│   ├── prompts/                          # LLM extraction prompt variants
│   │   └── (P0–P5: baseline, minimal, structured, reasoning, validation, framework-specific)
│   ├── evaluation/
│   │   └── evaluate_kgs.py              # KG quality evaluation
│   ├── ground_truth_scripts/             # Reference workflows (DO NOT EDIT)
│   │   ├── CrewAI/                       # 16 patterns
│   │   ├── AutoGen/                      # 6 patterns
│   │   ├── LangGraph/                    # 9 patterns
│   │   └── Mastra AI/                    # 35 patterns
│   └── generated_kgs/                    # Output KGs: <Framework>/<PromptID>/<Model>/*.ttl
│
└── kg_to_script/                         # Pipeline 2: KG → Script
    ├── src/
    │   ├── core/                         # Framework-agnostic extraction and canonical IR
    │   │   ├── extractor.py              # rdflib loading + SPARQL query engine
    │   │   ├── queries.py                # SPARQL queries over AgentO schema
    │   │   └── models.py                 # Pydantic canonical Intermediate Representation
    │   └── frameworks/                   # Per-framework adapters and generators
    │       ├── crewai/
    │       ├── autogen/
    │       ├── langgraph/
    │       └── mastra/
    ├── evaluation/
    │   ├── run.py                        # Per-framework OEC/WGI evaluation
    │   ├── interop_run.py                # Cross-framework interoperability evaluation
    │   └── metrics/
    │       ├── compilation.py            # Syntax verification
    │       └── dry_run.py                # Functional dry-run execution
    ├── tests/                            # Unit tests for extractors and adapters
    └── generated_projects/               # Generated executables (pipeline output)
        ├── output_crewai/
        ├── output_autogen/
        ├── output_langgraph/
        ├── output_mastra/
        └── output_interop/               # Cross-framework compilation targets
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- API credentials for at least one LLM provider (`OPENAI_API_KEY`, `GEMINI_API_KEY`, or `ANTHROPIC_API_KEY`) — required only for Pipeline 1 (KG generation). Pipeline 2 (KG-to-Script) and evaluation run without LLM access.

### Installation

Each pipeline is independently installable. Install only the pipeline(s) you intend to use.

```bash
git clone https://github.com/raviearjun/agentic-generator-paper.git
cd agentic-generator-paper

# Pipeline 1 environment
cd script_to_kg
python -m venv venv && source venv/bin/activate
pip install -e .
cd ..

# Pipeline 2 environment
cd kg_to_script
python -m venv venv && source venv/bin/activate
pip install -e .
cd ..
```

### Step 1 — Knowledge Graph Generation (Script → KG)

Extract AgentO-compliant KG instances from reference source code:

```bash
cd script_to_kg
source venv/bin/activate

# Single experiment: framework × prompt variant × LLM backend
python -m src.run_experiment --framework CrewAI --prompt P0 --model chatgpt

# Full experiment matrix (all frameworks × all prompts × all models)
python -m src.run_experiment --framework all --prompt all --model all
```

Output KGs are written to `script_to_kg/generated_kgs/<Framework>/<PromptID>/<Model>/`.

### Step 2 — Script Generation (KG → Script)

Compile AgentO KG instances into framework-native executable code:

```bash
cd kg_to_script
source venv/bin/activate

python -m src.frameworks.crewai.run
python -m src.frameworks.autogen.run
python -m src.frameworks.langgraph.run
python -m src.frameworks.mastra.run
```

Generated scripts are written to `kg_to_script/generated_projects/output_<framework>/`.

### Step 3 — Evaluation

Run the full validation suite (syntax verification, dry-run execution, OEC, WGI):

```bash
cd kg_to_script
source venv/bin/activate

# Per-framework evaluation (OEC, WGI, compilation, dry-run)
python -m evaluation.run --framework all

# Cross-framework interoperability evaluation
python -m evaluation.interop_run
```

Evaluation reports are written to:
- `kg_to_script/evaluation_reports/oec_wgi_results.json`
- `kg_to_script/evaluation_reports/oec_wgi_results.md`

---

## Relation to the Base Paper

The original ESWC 2025 paper demonstrated AgentO's utility through three SPARQL-based use cases: declarative pattern reconstruction, component reusability, and workflow auditing. This repository constitutes the generative extension referenced in the paper's future work section:

> *"as part of another research project, we aim to develop and maintain an open-source software that can (semi-automatically) translate AgentO workflows to specific target frameworks."*

The implementation provides empirical validation of AgentO's generative completeness, complementing the paper's descriptive and query-based validation with execution-level evidence.

---

## Citation

If this work or the AgentO ontology is used in research, please cite the ESWC 2025 paper:

```bibtex
@inproceedings{ekelhart2025agento,
  title     = {{AgentO}: An Ontology for Modeling Agentic {AI} Systems},
  author    = {Ekelhart, Andreas and Kurniawan, Kabul and Ekaputra, Fajar J. and Kiesling, Elmar},
  booktitle = {Proceedings of the Extended Semantic Web Conference (ESWC)},
  year      = {2025},
  doi       = {10.5281/zenodo.18342624},
  url       = {https://w3id.org/agentic-ai/onto}
}
```

---

## Developer Notes

Refer to [AGENTS.md](AGENTS.md) for workspace policies, pipeline editing rules, and validation workflow guidance.

Key invariants:
- `script_to_kg/` and `kg_to_script/` are independently installable; do not introduce cross-imports.
- Ground truth scripts in `script_to_kg/ground_truth_scripts/` are read-only reference material.
- Generated outputs (`generated_kgs/`, `generated_projects/`) are pipeline artifacts and should not be edited manually.
- SPARQL queries in `kg_to_script/src/core/queries.py` are tightly coupled to the AgentO schema; modifications to extraction logic require corresponding updates to framework adapters.
