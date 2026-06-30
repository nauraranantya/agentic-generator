# Mastraagentsystem

Collection of agents and tools composing the CLI assistant 'Dane' and associated workflows.

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
Mastraagentsystem/
├── src/
│   └── mastra/
│       ├── index.ts           # Mastra instance + registrations
│       ├── agents/            # Agent definitions
│       │   └── dane.ts
│       │   └── daneCommitMessage.ts
│       │   └── daneIssueLabeler.ts
│       │   └── daneLinkChecker.ts
│       │   └── danePackagePublisher.ts
│       │   └── daneNewContributor.ts
│       ├── tools/             # Tool definitions
│       │   └── toolExecaTool.ts
│       │   └── toolFsTool.ts
│       │   └── toolSlackMcp.ts
│       │   └── toolListEvents.ts
│       │   └── toolBrowserTool.ts
│       │   └── toolGoogleSearch.ts
│       │   └── toolReadPdf.ts
│       │   └── toolPnpmBuild.ts
│       │   └── toolPnpmChangesetStatus.ts
│       │   └── toolPnpmChangesetPublish.ts
│       │   └── toolActiveDistTag.ts
│       └── workflows/         # Workflow definitions
│           └── workflowCommitMessage.ts
│           └── workflowTelephoneGame.ts
│           └── workflowLinkChecker.ts
│           └── workflowChangelog.ts
│           └── workflowPackagePublisher.ts
│           └── workflowMessage.ts
│           └── workflowGithubIssueLabeler.ts
│           └── workflowGithubFirstContributor.ts
├── package.json
├── tsconfig.json
└── .env.example
```

---

## 🤖 Agents

### assistant

- **ID:** `dane`
- **Model:** `anthropic/claude-3-5-sonnet-20241022`
- **Tools:** toolExecaTool, toolFsTool, toolListEvents, toolBrowserTool, toolGoogleSearch, toolReadPdf

You are assistant....

### LLM Agent

- **ID:** `dane-commit-message`
- **Model:** `anthropic/claude-3-5-sonnet-20241022`
- **Tools:** toolFsTool

You are LLM Agent....

### LLM Agent

- **ID:** `dane-issue-labeler`
- **Model:** `anthropic/claude-3-5-sonnet-20241022`

You are LLM Agent....

### LLM Agent

- **ID:** `dane-link-checker`
- **Model:** `anthropic/claude-3-5-sonnet-20241022`
- **Tools:** toolSlackMcp

You are LLM Agent....

### LLM Agent

- **ID:** `dane-package-publisher`
- **Model:** `anthropic/claude-3-5-sonnet-20241022`
- **Tools:** toolPnpmBuild, toolPnpmChangesetStatus, toolPnpmChangesetPublish, toolActiveDistTag

You are LLM Agent....

### LLM Agent

- **ID:** `dane-new-contributor`
- **Model:** `anthropic/claude-3-5-sonnet-20241022`

You are LLM Agent....


---

## 🔧 Tools

### execaTool

Tool wrapping execa to run commands and stream output to console. Input: {command, args}. Output: {message}....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/toolExecaTool.ts`)

### fsTool

File system tool to read/write/append files....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/toolFsTool.ts`)

### mcpSlackClient

MCP client configured to run Slack container. Exposes tools for posting to Slack....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/toolSlackMcp.ts`)

### listEvents

Tool that lists calendar events by reading Mac Calendar via AppleScript and parsing into event objects....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/toolListEvents.ts`)

### browserTool

Opens a headless chromium browser, retrieves page content and returns chunked textual document representation....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/toolBrowserTool.ts`)

### googleSearch

Performs a Google search and returns a list of result URLs....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/toolGoogleSearch.ts`)

### readPDF

Reads PDF file and extracts textual content; validates file path and type....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/toolReadPdf.ts`)

### pnpmBuild

Build a package using pnpm run build at provided packagePath. Input: {name, packagePath}....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/toolPnpmBuild.ts`)

### pnpmChangesetStatus

Checks 'pnpm publish -r --dry-run --no-git-checks' to determine which packages need to be published. Returns array of package names....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/toolPnpmChangesetStatus.ts`)

### pnpmChangesetPublish

Publishes packages via pnpm changeset publish....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/toolPnpmChangesetPublish.ts`)

### activeDistTag

Sets an npm dist tag on a package using npm dist-tag add <pkg>@<version> latest....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/toolActiveDistTag.ts`)


---

## 🔄 Workflows

### commit-message workflow

Workflow to generate and optionally commit a sensible git commit message for staged changes.

**Steps:** 0

### telephoneGame workflow

Play a game of telephone: starts a message, passes it through participants with optional modification by an agent and supports suspension/resume awaiting user confirmation.

**Steps:** 0

### link-checker workflow

Checks a target URL for broken links using linkinator and posts results to Slack via MCP.

**Steps:** 0

### changelog workflow

Generates weekly changelogs by scanning a predefined list of module paths, computing diffs between two dates, and asking an agent to summarize per-module changes; posts combined changelog to Slack.

**Steps:** 0

### pnpm-changset-publisher

Builds all packages, publishes changesets and sets dist-tags for monorepo packages.

**Steps:** 0

### message (entry) workflow

Interactive chat workflow: prompt user for message and then have dane agent respond (streaming or non-streaming).

**Steps:** 0

### github-issue-labeler workflow

Fetch GitHub issue contents, obtain available labels, ask agent to select labels and apply them via GitHub integration.

**Steps:** 0

### github-first-contributor-message workflow

On first contributor PR, generate welcoming message combining PR title, body, diff and Mastra docs; post as PR comment.

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
