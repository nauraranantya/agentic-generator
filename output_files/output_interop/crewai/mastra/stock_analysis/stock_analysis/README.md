# StockAnalysisCrew

Team that coordinates a set of LLM agents and tasks to perform stock/filings/research analysis for a given company ticker (example: AMZN).

**Auto-generated from AgentO Knowledge Graph**  
Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
npm install
```

### 2. Configure Environment

Copy `.env.example` to `.env` and fill in your API keys:

```bash
cp .env.example .env
```

### 3. Run the Project

```bash
npm run dev
```

---

## 📦 Project Structure

```
StockAnalysisCrew/
├── src/
│   └── mastra/
│       ├── index.ts           # Mastra instance + registrations
│       ├── agents/            # Agent definitions
│       │   └── financialAgent.ts
│       │   └── financialAnalystAgent.ts
│       │   └── researchAnalystAgent.ts
│       │   └── investmentAdvisorAgent.ts
│       ├── tools/             # Tool definitions
│       │   └── toolCalculator.ts
│       │   └── toolScrapeWebsite.ts
│       │   └── toolWebsiteSearch.ts
│       │   └── toolTxtSearch.ts
│       │   └── sec10KToolGeneric.ts
│       │   └── sec10KToolAmzn.ts
│       │   └── sec10QToolGeneric.ts
│       │   └── sec10QToolAmzn.ts
│       └── workflows/         # Workflow definitions
│           └── stockAnalysisWorkflow.ts
├── package.json
├── tsconfig.json
└── .env.example
```

---

## 🤖 Agents

### The Best Financial Analyst

- **ID:** `financial_agent`
- **Model:** `openai/gpt-4o-mini`
- **Tools:** toolCalculator, toolScrapeWebsite, toolWebsiteSearch, sec10KToolAmzn, sec10QToolAmzn

This prompt is used as the agent/system instruction for the financial agent to guide independent behaviour....

### The Best Financial Analyst

- **ID:** `financial_analyst_agent`
- **Model:** `openai/gpt-4o-mini`
- **Tools:** toolCalculator, toolScrapeWebsite, toolWebsiteSearch, sec10KToolGeneric, sec10QToolGeneric

This prompt is produced from the second factory for financial_analyst_agent in the code (duplicate configuration)....

### Staff Research Analyst

- **ID:** `research_analyst_agent`
- **Model:** `openai/gpt-4o-mini`
- **Tools:** toolScrapeWebsite, sec10KToolAmzn, sec10QToolAmzn

System prompt for the research analyst agent....

### Private Investment Advisor

- **ID:** `investment_advisor_agent`
- **Model:** `openai/gpt-4o-mini`
- **Tools:** toolCalculator, toolScrapeWebsite, toolWebsiteSearch

System prompt for the investment advisor agent....


---

## 🔧 Tools

### CalculatorTool

Calculator tool (from src/stock_analysis/tools/calculator_tool.py).
    Purpose: perform mathematical calculations expressed as arithmetic expressions (examples: '200*7', '5000/2*10').
    Implementat...

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/toolCalculator.ts`)

### ScrapeWebsiteTool

Tool used to fetch and convert HTML pages into text for downstream processing. Referenced from crewai_tools usage in the crew....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/toolScrapeWebsite.ts`)

### WebsiteSearchTool

Tool used for general website search (referenced from crewai_tools in the crew)....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/toolWebsiteSearch.ts`)

### TXTSearchTool

Tool used for searching plaintext resources (referenced from crewai_tools in the crew)....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/toolTxtSearch.ts`)

### SEC10KTool (generic)

A RAG-style tool for semantic search in 10-K filings (class src/stock_analysis/tools/sec_tools.py).
    Default args_schema: requires search_query and stock_name.
    Behavior: when initialized with a...

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/sec10KToolGeneric.ts`)

### SEC10KTool(AMZN)

Instance of SEC10KTool initialized with stock_name='AMZN'. On init it attempted to fetch AMZN's latest 10-K, converted it to text, cleaned non-alphanumeric characters, and added the text to its intern...

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/sec10KToolAmzn.ts`)

### SEC10QTool (generic)

A RAG-style tool for semantic search in 10-Q filings (class src/stock_analysis/tools/sec_tools.py).
    Default args_schema: requires search_query and stock_name.
    Behavior: when initialized with a...

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/sec10QToolGeneric.ts`)

### SEC10QTool(AMZN)

Instance of SEC10QTool initialized with stock_name='AMZN'. On init it attempted to fetch AMZN's latest 10-Q, converted it to text, cleaned non-alphanumeric characters, and added the text to its intern...

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/sec10QToolAmzn.ts`)


---

## 🔄 Workflows

### Stock Analysis Sequential Workflow

Workflow pattern representing the crew's intended sequential pipeline: research -> filings_analysis -> financial_analysis -> recommend

**Steps:** 4
1. research
2. filings_analysis
3. financial_analysis
4. recommend


---

## 📝 Next Steps

1. **Implement tools:** Replace `throw new Error(...)` in tool files with actual implementations
2. **Implement workflow steps:** Add logic to each step's `execute` function
3. **Test agents:** Use Mastra Studio or write test scripts
4. **Deploy:** Follow [Mastra deployment guide](https://mastra.ai/docs/deployment)

---

## 📚 Resources

- [Mastra Documentation](https://mastra.ai/docs)
- [AgentO Ontology](https://w3id.org/agentic-ai/onto)
- [Mastra Discord Community](https://discord.gg/BTYqqHKUrf)

---

**Generated by:** Agentic AI Framework Generator  
**Source:** AgentO Knowledge Graph → Mastra AI TypeScript
