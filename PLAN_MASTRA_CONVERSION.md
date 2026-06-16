# Rencana Pengembangan: KG → Mastra AI Code Generator

## 1. Ringkasan Proyek

### Latar Belakang
Repository ini merupakan **ekstensi dari paper sebelumnya** yang mengonversi kode agentic AI → Knowledge Graph (KG) menggunakan ontologi AgentO. Penelitian ini membalikkan arah: **KG → Kode** — membaca file `.ttl` (Turtle/RDF) dan menghasilkan proyek framework yang dapat dijalankan.

### Status Saat Ini
- ✅ **CrewAI** (Python): Pipeline 3-layer sudah selesai (`src/crewai/`)
  - Layer 1: SPARQL Extraction (`extractor.py`)
  - Layer 2: Pydantic IR (`models.py`)
  - Layer 3: File Generation (`generator.py` + Jinja2 templates)
- ❌ **Mastra AI** (TypeScript): Belum ada pipeline konversi

### Target
Membangun pipeline konversi `KG (.ttl) → Mastra AI TypeScript Project` dengan arsitektur 3-layer yang sama, menggunakan implementasi CrewAI sebagai acuan.

---

## 2. Analisis Perbandingan: CrewAI vs Mastra AI

### 2.1 Perbedaan Fundamental

| Aspek | CrewAI (Python) | Mastra AI (TypeScript) |
|-------|----------------|----------------------|
| **Bahasa** | Python | TypeScript |
| **Package Manager** | pip / pyproject.toml | npm / package.json |
| **Agent Definition** | YAML config + Python class | TypeScript `new Agent({...})` |
| **Workflow** | `Process.sequential` / `Process.hierarchical` | `createWorkflow().then().commit()` |
| **Task** | YAML config + Python method | `createStep({...})` dengan input/output schema |
| **Tool** | `crewai_tools` imports | `createTool({...})` dengan Zod schema |
| **LLM Config** | String `"provider/model"` | `openai('gpt-4o')` / model router `'provider/model-name'` |
| **Memory** | Implisit (flag) | Eksplisit (`Memory` class + storage backend) |
| **Schema** | Tidak ada | Zod schema (input/output per step & tool) |
| **Control Flow** | Sequential / Hierarchical saja | Sequential, Parallel, Branch, Loop, Suspend/Resume |
| **Entry Point** | `main.py` + `crew.kickoff()` | `index.ts` + `new Mastra({...})` |

### 2.2 Pemetaan Ontologi → Mastra AI

| Ontologi (KG) | CrewAI Output | Mastra AI Output |
|---------------|--------------|-----------------|
| `:Team` | `@CrewBase` class | `new Mastra({...})` di `index.ts` |
| `:LLMAgent` | `@agent` method + `agents.yaml` | `new Agent({...})` di `agents/*.ts` |
| `:Task` | `@task` method + `tasks.yaml` | `createStep({...})` di `workflows/*.ts` |
| `:Tool` | Tool import + instantiation | `createTool({...})` di `tools/*.ts` |
| `:WorkflowPattern` | `Process.sequential` | `createWorkflow({...}).then().commit()` |
| `:WorkflowStep` | Task ordering | `.then(step)` / `.parallel()` / `.branch()` |
| `:LanguageModel` | `llm=` parameter | `model:` property (model router string) |
| `:Prompt` | `agents.yaml` backstory | `instructions:` string |
| `:Memory` | _(tidak ada)_ | `Memory` instance + storage config |
| `:Config` | `.env` / YAML config | `.env` / TypeScript config objects |
| `:Capability` | _(deskripsi)_ | Tool description |

---

## 3. Arsitektur Pipeline: 3-Layer

```
KG (.ttl)
    │
    ▼
┌─────────────────────────────────┐
│  Layer 1: SPARQL Extraction     │  src/mastra/extractor.py
│  rdflib + SPARQL queries        │
│  → Extract agents, tools,       │
│    workflows, steps, memory,    │
│    schemas, configs              │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│  Layer 2: Pydantic IR           │  src/mastra/models.py
│  MastraProject, AgentModel,     │
│  StepModel, ToolModel,          │
│  WorkflowModel, MemoryModel     │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│  Layer 3: File Generation       │  src/mastra/generator.py
│  Jinja2 templates →             │    + templates/*.ts.j2
│  TypeScript files               │
└──────────────┬──────────────────┘
               │
               ▼
output_files/output_mastra/{project_name}/
├── src/
│   └── mastra/
│       ├── index.ts           ← Mastra instance + registrations
│       ├── agents/
│       │   └── {agent}.ts     ← Agent definitions
│       ├── tools/
│       │   └── {tool}.ts      ← Tool definitions (createTool)
│       └── workflows/
│           └── {workflow}.ts  ← Workflow + step definitions
├── package.json
├── tsconfig.json
├── .env.example
└── README.md
```

---

## 4. Rencana Implementasi Detail

### Fase 1: Layer 2 — Pydantic IR Models (`src/mastra/models.py`)

**Prioritas: TINGGI** | Fondasi untuk seluruh pipeline

Buat model data yang merepresentasikan semua konstruk Mastra AI:

```python
# Model-model yang perlu dibuat:

class MastraProject(BaseModel):
    """Top-level project — setara CrewProject"""
    project_name: str
    project_var_name: str
    description: str
    agents: List[MastraAgentModel]
    tools: List[MastraToolModel]
    workflows: List[WorkflowModel]
    memory_configs: List[MemoryModel]        # BARU - tidak ada di CrewAI
    language_models: List[LanguageModelModel]
    env_vars: List[ConfigModel]

class MastraAgentModel(BaseModel):
    """KG :LLMAgent → Mastra Agent"""
    iri: str
    var_name: str
    agent_id: str                            # :agentID
    name: str                                # rdfs:label
    instructions: str                        # :agentPrompt → :promptInstruction
    model: str                               # :useLanguageModel → model router string
    tool_var_names: List[str]                # :agentToolUsage
    memory_var_name: Optional[str]           # BARU - :hasKnowledge → Memory
    max_retries: Optional[int]               # BARU - dari Config

class MastraToolModel(BaseModel):
    """KG :Tool → Mastra createTool()"""
    iri: str
    var_name: str
    tool_id: str                             # rdfs:label (tool ID)
    description: str
    input_schema: Optional[str]              # BARU - Zod schema dari deskripsi
    output_schema: Optional[str]             # BARU - Zod schema dari deskripsi
    execute_description: str                 # Logika eksekusi dari deskripsi
    configs: List[ToolConfigModel]
    is_custom: bool                          # True = perlu implementasi manual

class WorkflowModel(BaseModel):
    """KG :WorkflowPattern → Mastra createWorkflow()"""
    iri: str
    var_name: str
    workflow_id: str                         # rdfs:label
    description: str
    input_schema: Optional[str]              # BARU
    output_schema: Optional[str]             # BARU
    steps: List[StepModel]
    control_flow: ControlFlowType            # BARU - sequential/parallel/branch/loop

class StepModel(BaseModel):
    """KG :WorkflowStep → Mastra createStep()"""
    iri: str
    var_name: str
    step_id: str
    step_order: int
    description: str
    input_schema: Optional[str]              # BARU - dari Prompt :promptInputData
    output_schema: Optional[str]             # BARU - dari Prompt :promptOutputIndicator
    execute_description: str                 # Logika eksekusi dari deskripsi
    agent_var_name: Optional[str]            # Jika step menggunakan agent
    tool_var_name: Optional[str]             # Jika step menggunakan tool
    is_suspend_resume: bool                  # BARU - deteksi suspend/resume
    suspend_schema: Optional[str]            # BARU
    resume_schema: Optional[str]             # BARU

class MemoryModel(BaseModel):
    """KG :Memory → Mastra Memory config"""
    iri: str
    var_name: str
    storage_type: str                        # mongodb / libsql / pg / upstash
    storage_config: List[ConfigModel]
    embedder_model: Optional[str]
    working_memory_enabled: bool
    semantic_recall: Optional[dict]

class ControlFlowType(str, Enum):
    SEQUENTIAL = "sequential"
    PARALLEL = "parallel"
    BRANCHING = "branching"
    LOOP = "loop"
    MIXED = "mixed"
```

**Tugas:**
- [ ] `src/mastra/__init__.py` — Package init
- [ ] `src/mastra/models.py` — Semua model di atas

---

### Fase 2: Layer 1 — SPARQL Extraction (`src/mastra/extractor.py`)

**Prioritas: TINGGI** | Parsing KG ke IR

Referensi langsung dari `src/crewai/extractor.py`, tapi dengan query SPARQL tambahan untuk fitur Mastra:

#### 2.1 Query SPARQL yang Bisa Di-reuse dari CrewAI
- `TEAM_QUERY` → Extract `:Team` (= Mastra system)
- `LLM_QUERY` → Extract `:LanguageModel`
- `TOOLS_QUERY` + `TOOL_CONFIGS_QUERY` → Extract `:Tool`
- `AGENTS_QUERY` → Extract `:LLMAgent` (adaptasi untuk Mastra properties)
- `WORKFLOW_QUERY` → Extract `:WorkflowStep` ordering
- `ENV_CONFIG_QUERY` → Extract API keys

#### 2.2 Query SPARQL BARU untuk Mastra
```sparql
# ── Agent Instructions (Mastra pakai promptInstruction, bukan promptContext) ──
AGENT_INSTRUCTIONS_QUERY = """
SELECT ?agent ?instruction
WHERE {
    ?agent a :LLMAgent ;
           :agentPrompt ?prompt .
    ?prompt :promptInstruction ?instruction .
}
"""

# ── Tool I/O Schemas (parsed dari deskripsi) ──
TOOL_SCHEMA_QUERY = """
SELECT ?tool ?desc
WHERE {
    ?tool a :Tool .
    ?tool dcterms:description ?desc .
    FILTER NOT EXISTS { ?tool a :LLMAgent }
}
"""

# ── Memory Instances ──
MEMORY_QUERY = """
SELECT ?mem ?label ?desc
WHERE {
    ?mem a :Memory .
    OPTIONAL { ?mem rdfs:label ?label }
    OPTIONAL { ?mem dcterms:description ?desc }
}
"""

# ── Agent-Memory Linkage ──
AGENT_MEMORY_QUERY = """
SELECT ?agent ?mem
WHERE {
    ?agent a :LLMAgent ;
           :hasKnowledge ?mem .
    ?mem a :Memory .
}
"""

# ── Workflow Pattern (with sub-patterns for nested workflows) ──
WORKFLOW_PATTERN_QUERY = """
SELECT ?wp ?label ?desc
WHERE {
    ?wp a :WorkflowPattern .
    OPTIONAL { ?wp rdfs:label ?label }
    OPTIONAL { ?wp dcterms:description ?desc }
}
"""

# ── Step Schemas (dari Prompt terkait) ──
STEP_SCHEMA_QUERY = """
SELECT ?step ?inputData ?outputIndicator ?instruction ?context
WHERE {
    ?step a :WorkflowStep ;
          :hasAssociatedTask ?task .
    {
        { ?task :taskPrompt ?prompt }
        UNION
        { ?task :hasPrompt ?prompt }
        UNION
        { ?step :taskPrompt ?prompt }
    }
    OPTIONAL { ?prompt :promptInputData ?inputData }
    OPTIONAL { ?prompt :promptOutputIndicator ?outputIndicator }
    OPTIONAL { ?prompt :promptInstruction ?instruction }
    OPTIONAL { ?prompt :promptContext ?context }
}
"""

# ── Suspend/Resume Detection ──
SUSPEND_RESUME_QUERY = """
SELECT ?step ?context
WHERE {
    ?step a :WorkflowStep ;
          :hasAssociatedTask ?task .
    { ?task :taskPrompt ?prompt } UNION { ?task :hasPrompt ?prompt }
    ?prompt :promptContext ?context .
    FILTER(CONTAINS(LCASE(?context), "suspend"))
}
"""

# ── Memory Config Details ──
MEMORY_CONFIG_QUERY = """
SELECT ?mem ?key ?value
WHERE {
    ?mem a :Memory ;
         :hasConfig ?cfg .
    ?cfg :configKey ?key ;
         :configValue ?value .
}
"""
```

#### 2.3 Fungsi Parsing Khusus Mastra

```python
def _parse_tool_schema(description: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Parse input/output schema dari deskripsi tool.
    KG Mastra menyimpan schema sebagai literal di deskripsi:
      'Input schema: { ingredient: string }'
      'Output: numeric result'
    → Konversi ke Zod schema string
    """

def _infer_model_router_string(label: str) -> str:
    """
    Konversi LanguageModel rdfs:label ke Mastra model router format.
    'openai:gpt-4o' → 'openai/gpt-4o'
    'anthropic:claude-3-5-sonnet-20241022' → 'anthropic/claude-3-5-sonnet-20241022'
    'google:gemini-2.0-flash-001' → 'google/gemini-2.0-flash-001'
    """

def _detect_control_flow(workflow_desc: str, steps: List) -> ControlFlowType:
    """
    Analisis deskripsi workflow untuk mendeteksi control flow type.
    Cek keyword: 'parallel', 'branch', 'loop', 'doUntil', 'map'
    """

def _detect_suspend_resume(step_desc: str, prompt_context: str) -> bool:
    """
    Deteksi apakah step memerlukan suspend/resume.
    Cek keyword: 'suspend', 'resume', 'user input', 'interactive'
    """

def _parse_memory_storage_type(description: str) -> str:
    """
    Infer storage backend dari deskripsi Memory.
    'MongoDB' → 'mongodb'
    'LibSQL' → 'libsql'
    'PostgreSQL' → 'pg'
    'Upstash' → 'upstash'
    """
```

**Tugas:**
- [ ] `src/mastra/extractor.py` — Semua query + fungsi extraction
- [ ] Fungsi utama: `extract_mastra_project(ttl_path: str) -> MastraProject`

---

### Fase 3: Layer 3 — File Generation (`src/mastra/generator.py` + templates)

**Prioritas: TINGGI** | Menghasilkan kode TypeScript

#### 3.1 Template Jinja2

**`templates/index.ts.j2`** — Entry point Mastra
```typescript
// Template menghasilkan:
import { Mastra } from '@mastra/core/mastra'
import { agent1 } from './agents/agent1'
import { workflow1 } from './workflows/workflow1'

export const mastra = new Mastra({
  agents: { agent1 },
  workflows: { workflow1 },
})
```

**`templates/agent.ts.j2`** — Agent definition
```typescript
// Template menghasilkan:
import { Agent } from '@mastra/core/agent'
import { tool1 } from '../tools/tool1'

export const myAgent = new Agent({
  id: 'my-agent',
  name: 'My Agent',
  instructions: `...`,
  model: 'openai/gpt-4o',
  tools: { tool1 },
})
```

**`templates/tool.ts.j2`** — Tool definition
```typescript
// Template menghasilkan:
import { createTool } from '@mastra/core/tools'
import { z } from 'zod'

export const myTool = createTool({
  id: 'my-tool',
  description: '...',
  inputSchema: z.object({ ... }),
  outputSchema: z.object({ ... }),
  execute: async ({ inputData }) => {
    // TODO: Implement tool logic
    // Description: ...
    return { ... }
  },
})
```

**`templates/workflow.ts.j2`** — Workflow + steps
```typescript
// Template menghasilkan:
import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

const step1 = createStep({
  id: 'step-1',
  inputSchema: z.object({ ... }),
  outputSchema: z.object({ ... }),
  execute: async ({ inputData }) => {
    // TODO: Implement step logic
    return { ... }
  },
})

export const myWorkflow = createWorkflow({
  id: 'my-workflow',
  inputSchema: z.object({ ... }),
  outputSchema: z.object({ ... }),
})
  .then(step1)
  .commit()
```

**`templates/package.json.j2`** — Dependencies
```json
{
  "name": "{{ project_var_name }}",
  "dependencies": {
    "@mastra/core": "latest",
    "zod": "^3.23.0"
    // + conditional: @mastra/memory, storage adapters
  }
}
```

**`templates/tsconfig.json.j2`** — TypeScript config (static template)

**`templates/env.example.j2`** — Environment variables

#### 3.2 Generator Functions

```python
def generate_project(project: MastraProject, output_dir: str) -> str:
    """Generate complete Mastra project directory."""

def _generate_index_ts(project: MastraProject) -> str:
    """Generate src/mastra/index.ts — Mastra registration."""

def _generate_agent_ts(agent: MastraAgentModel, project: MastraProject) -> str:
    """Generate per-agent TypeScript file."""

def _generate_tool_ts(tool: MastraToolModel) -> str:
    """Generate per-tool TypeScript file with createTool()."""

def _generate_workflow_ts(workflow: WorkflowModel, project: MastraProject) -> str:
    """Generate workflow TypeScript file with steps + control flow."""

def _generate_package_json(project: MastraProject) -> str:
    """Generate package.json with auto-inferred dependencies."""

def _generate_env_example(project: MastraProject) -> str:
    """Generate .env.example with required API keys."""
```

**Tugas:**
- [ ] `src/mastra/generator.py` — Semua fungsi generation
- [ ] `src/mastra/templates/index.ts.j2`
- [ ] `src/mastra/templates/agent.ts.j2`
- [ ] `src/mastra/templates/tool.ts.j2`
- [ ] `src/mastra/templates/workflow.ts.j2`
- [ ] `src/mastra/templates/package.json.j2`
- [ ] `src/mastra/templates/tsconfig.json.j2`
- [ ] `src/mastra/templates/env.example.j2`

---

### Fase 4: Runner & Testing (`src/mastra/run.py`)

**Prioritas: MENENGAH**

```python
# src/mastra/run.py
# Batch-process kgs_extended/Mastra AI/*.ttl → output_files/output_mastra/

def process_single(kg_path: str, output_dir: str) -> str
def main()  # CLI: python -m src.mastra.run [file.ttl]
```

**Tugas:**
- [ ] `src/mastra/run.py` — CLI runner (copy-adapt dari `src/crewai/run.py`)
- [ ] Testing manual: jalankan pada 5 KG representatif:
  - `quick-start_instances.ttl` (simple agent)
  - `weather-agent_instances.ttl` (agent + tools + workflow)
  - `agent_instances.ttl` (complex multi-agent + memory)
  - `workflow-with-suspend-resume_instances.ttl` (suspend/resume)
  - `memory-with-mongodb_instances.ttl` (memory + storage)

---

## 5. Tantangan & Strategi Penanganan

### 5.1 Schema Extraction dari Deskripsi Natural Language
**Masalah:** KG Mastra menyimpan Zod schema sebagai teks literal di `dcterms:description`.
**Contoh:** `"Input schema: { ingredient: string }"`
**Strategi:**
- Buat regex parser untuk pola umum: `{ key: type, key2: type }`
- Map ke Zod: `string` → `z.string()`, `number` → `z.number()`, `boolean` → `z.boolean()`
- Fallback: generate `z.any()` + komentar TODO jika parsing gagal

### 5.2 Complex Control Flow
**Masalah:** Mastra mendukung `.parallel()`, `.branch()`, `.doUntil()` yang tidak ada di CrewAI.
**Strategi:**
- Fase awal: hanya support `.then()` (sequential) — **MVP**
- Fase lanjutan: deteksi keyword "parallel"/"branch"/"loop" di deskripsi workflow
- Generate komentar TODO untuk control flow yang belum disupport

### 5.3 Suspend/Resume
**Masalah:** Beberapa step memerlukan user input (suspend/resume).
**Strategi:**
- Deteksi dari `promptContext` yang mengandung "suspend"
- Generate step dengan `suspend()` call dan komentar
- Generate contoh resume code di file terpisah

### 5.4 Memory & Storage Backend
**Masalah:** Berbagai storage backend (MongoDB, LibSQL, PostgreSQL, Upstash).
**Strategi:**
- Parse storage type dari deskripsi Memory
- Generate import yang sesuai (`@mastra/memory`, storage adapter)
- Generate config dengan env variable placeholders

### 5.5 Tool Implementation
**Masalah:** Tool memerlukan actual implementation (fetch API, dll).
**Strategi:**
- Generate skeleton `createTool()` dengan schema yang benar
- Taruh deskripsi logika di komentar `// TODO:`
- Untuk tool yang memanggil API eksternal, generate `fetch()` stub

---

## 6. Urutan Pengerjaan (Milestone)

### Milestone 1: MVP — Agent + Tool Sederhana ✅ **SELESAI**
**Target:** Bisa generate proyek dari `quick-start_instances.ttl`
- [x] Rencana (dokumen ini)
- [x] `models.py` — MastraProject, MastraAgentModel, MastraToolModel, LanguageModelModel
- [x] `extractor.py` — Query basic (Team, Agent, Tool, LLM)
- [x] `generator.py` + templates — index.ts, agent.ts, tool.ts, package.json, tsconfig, env, README
- [x] `run.py` — Single file & batch runner
- [x] Test: `quick-start_instances.ttl` → proyek Mastra yang valid
- [x] **BONUS:** Batch test 35 KG files → 19+ projects generated successfully!

### Milestone 2: Workflow Sequential ✅ **SELESAI**
**Target:** Bisa generate workflow dengan steps sequential
- [x] `models.py` — WorkflowModel, StepModel (sudah ada dari Milestone 1)
- [x] `extractor.py` — Query WorkflowPattern, WorkflowStep, step schemas (multi-source)
- [x] `generator.py` + `workflow.ts.j2` — Sequential `.then()` chain + agent/tool imports
- [x] Test: `weather-agent_instances.ttl` → 2 workflows, 5 steps
- [x] **BONUS:** 40 workflow files generated across 26 successful projects!

### Milestone 3: Memory & Advanced Config ✅ **SELESAI**
**Target:** Generate memory config dan storage setup
- [x] `models.py` — MemoryModel (update: tambah `last_messages`, `semantic_recall_top_k/message_range/enabled`, `working_memory_template/scope`, `token_limit`, `vector_type/config`)
- [x] `extractor.py` — `_extract_memory()`, `_parse_memory_from_configs()`, `_is_storage_tool()`, agent-memory linkage via `AGENT_MEMORY_QUERY`, storage-tool detection
- [x] `generator.py` — `_generate_memory_files()`, storage helpers (`_storage_class`, `_storage_config_entries`, `_vector_config_entries`), env vars update, storage tool skip
- [x] `templates/memory.ts.j2` — Memory instance dengan storage backend (LibSQLStore/PostgresStore/MongoDBStore/UpstashStore), options, working memory, semantic recall
- [x] `templates/agent.ts.j2` — Memory import + `memory:` property
- [x] `templates/index.ts.j2` — Memory import + registration di Mastra instance
- [x] Test: 10 KG dengan Memory instances → 11 memory files di 26 proyek berhasil
- [x] **Storage types supported:** libsql (default), pg, mongodb, upstash
- [x] **Config patterns supported:** simple keys, namespaced keys, inline JSON options, storage type dari description fallback

### Milestone 4: Complex Workflows ✅ **SELESAI**
**Target:** Support parallel, branch, suspend/resume
- [x] `models.py` — ControlFlowType, suspend/resume fields
- [x] `extractor.py` — Detect control flow patterns
- [x] `generator.py` + `workflow.ts.j2` — `.parallel()`, `.branch()`, `suspend()` generation
- [x] Test: `workflow-with-suspend-resume_instances.ttl`, `agent_instances.ttl`

### Milestone 5: Batch Processing & Validation ✅ **SELESAI**
**Target:** Process semua 35 KG Mastra
- [x] `run.py` — Batch mode untuk semua `kgs_extended/Mastra AI/*.ttl`
- [x] Validasi: TypeScript syntax check (`tsc --noEmit`)
- [x] Laporan: success rate, error cases, coverage metrics
- [x] Dokumentasi: README update (dan Report Artifact)

---

## 7. Struktur File Akhir

```
src/
├── crewai/                    # ← Sudah ada (referensi)
│   ├── __init__.py
│   ├── extractor.py
│   ├── models.py
│   ├── generator.py
│   ├── run.py
│   └── templates/
│       ├── crew.py.j2
│       └── main.py.j2
│
└── mastra/                    # ← BARU (target pengembangan)
    ├── __init__.py
    ├── models.py              # Layer 2: Pydantic IR
    ├── extractor.py           # Layer 1: SPARQL extraction
    ├── generator.py           # Layer 3: File generation
    ├── run.py                 # CLI runner
    └── templates/
        ├── index.ts.j2        # Mastra entry point
        ├── agent.ts.j2        # Agent definition
        ├── tool.ts.j2         # Tool definition (createTool)
        ├── workflow.ts.j2     # Workflow + steps
        ├── package.json.j2    # npm dependencies
        ├── tsconfig.json.j2   # TypeScript config
        └── env.example.j2     # Environment variables
```

---

## 8. Referensi

- **CrewAI Pipeline (referensi utama):** `src/crewai/`
- **Ontologi:** `agentO.ttl`
- **KG Input:** `kgs_extended/Mastra AI/*.ttl` (35 file)
- **Mastra AI Docs:** https://mastra.ai/docs
  - Agents: https://mastra.ai/docs/agents/overview
  - Tools: https://mastra.ai/docs/agents/using-tools
  - Workflows: https://mastra.ai/docs/workflows/overview
  - Memory: https://mastra.ai/docs/memory/overview
- **Paper:** `paper/K-CAP_2025_paper_25.pdf`, `paper/paper-latest.pdf`
