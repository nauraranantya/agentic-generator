# ExpandIdeaCrewteam

Derived from src/landing_page_generator/crew.py ExpandIdeaCrew class. Process: sequential (expand_idea -> refine_idea).

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
ExpandIdeaCrewteam/
├── src/
│   └── mastra/
│       ├── index.ts           # Mastra instance + registrations
│       ├── agents/            # Agent definitions
│       │   └── seniorIdeaAnalyst.ts
│       │   └── seniorStrategist.ts
│       │   └── seniorReactEngineer.ts
│       │   └── seniorContentEditor.ts
│       ├── tools/             # Tool definitions
│       │   └── searchInternetTool.ts
│       │   └── scrapeWebsiteTool.ts
│       │   └── writeFileTool.ts
│       │   └── learnTemplatesTool.ts
│       │   └── copyTemplateTool.ts
│       │   └── readFileTool.ts
│       │   └── listDirectoryTool.ts
│       │   └── fileManagementToolkit.ts
│       └── workflows/         # Workflow definitions
│           └── expandIdeaWorkflowPattern.ts
│           └── chooseTemplateWorkflowPattern.ts
│           └── createContentWorkflowPattern.ts
│           └── landingPageWorkflowPattern.ts
├── package.json
├── tsconfig.json
└── .env.example
```

---

## 🤖 Agents

### Senior Idea Analyst

- **ID:** `senior_idea_analyst`
- **Model:** `openai/gpt-4`
- **Tools:** searchInternetTool, scrapeWebsiteTool

Understand and expand the idea into a comprehensive idea report, detailing value proposition and features....

### Senior Communications Strategist

- **ID:** `senior_strategist`
- **Model:** `openai/gpt-4`
- **Tools:** searchInternetTool, scrapeWebsiteTool

Provide WHY, HOW, WHAT messaging and core message for the idea....

### Senior React Engineer

- **ID:** `senior_react_engineer`
- **Model:** `openai/gpt-4`
- **Tools:** searchInternetTool, scrapeWebsiteTool, writeFileTool, learnTemplatesTool, copyTemplateTool, readFileTool, listDirectoryTool

Select a Tailwind template that fits the idea and copy it into the working folder; then update components....

### Senior Content Editor

- **ID:** `senior_content_editor`
- **Model:** `openai/gpt-4`
- **Tools:** writeFileTool, readFileTool, listDirectoryTool

Produce content for components, update components, and QA them according to rules....


---

## 🔧 Tools

### Search the internet (SearchTools.search_internet)

Performs internet search using an external search API (serper.dev). Requires SERPER_API_KEY environment variable....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/searchInternetTool.ts`)

### Scrape website content (BrowserTools.scrape_and_summarize_website)

Scrapes website HTML via browserless API and summarizes content using an internal summarization Task. Requires BROWSERLESS_API_KEY environment variable....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/scrapeWebsiteTool.ts`)

### Write file to workdir (FileTools.write_file)

Writes files into ./workdir with path sanitization and allowed extensions....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/writeFileTool.ts`)

### Learn landing page options (TemplateTools.learn_landing_page_options)

Reads config/templates.json to list available templates....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/learnTemplatesTool.ts`)

### Copy landing page template to project folder (TemplateTools.copy_landing_page_template_to_project_folder)

Copies a template folder from ./templates to ./workdir with safety checks....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/copyTemplateTool.ts`)

### Read file (file management toolkit: read_file)

Read file contents from workdir (used by agent toolkits)....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/readFileTool.ts`)

### List directory (file management toolkit: list_directory)

List directories in workdir (used by agent toolkits)....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/listDirectoryTool.ts`)

### File management toolkit container (provides read_file, list_directory tools)

In the code this is an instantiation of FileManagementToolkit(root_dir='workdir', selected_tools=['read_file','list_directory']). Modeled here as a Tool-like resource containing ReadFileTool and ListD...

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/fileManagementToolkit.ts`)


---

## 🔄 Workflows

### Expand Idea workflow pattern

Pattern contains two sequential steps: expand_idea then refine_idea.

**Steps:** 2
1. expand_idea_task
2. refine_idea_task

### Choose Template workflow pattern

Select a template, copy it to workdir, then determine components to update.

**Steps:** 2
1. choose_template_task
2. update_page_task

### Create Content workflow pattern

Produce component content, write components, and QA them.

**Steps:** 3
1. component_content_task
2. update_component_task
3. qa_component_task

### Landing page overall workflow

Top-level sequence: ExpandIdea -> ChooseTemplate -> CreateContent. ExpandIdeaWorkflowPattern is the first sub-pattern; nextPattern points to the subsequent pattern.

**Steps:** 0


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
