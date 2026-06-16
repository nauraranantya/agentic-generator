# MastraAgentSystem

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
MastraAgentSystem/
├── src/
│   └── mastra/
│       ├── index.ts           # Mastra instance + registrations
│       ├── agents/            # Agent definitions
│       │   └── agentDane.ts
│       │   └── agentDaneCommitMessage.ts
│       │   └── agentDaneIssueLabeler.ts
│       │   └── agentDaneLinkChecker.ts
│       │   └── agentDanePackagePublisher.ts
│       │   └── agentDaneNewContributor.ts
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

### dane

- **ID:** `dane`
- **Model:** `anthropic/claude-3-5-sonnet-20241022`
- **Tools:** toolExecaTool, toolFsTool, toolListEvents, toolBrowserTool, toolGoogleSearch, toolReadPdf

You are Dane, my assistant and one of my best friends. We are an ace team!
You help me with my code, write tests, and even deploy my code to the cloud!

DO NOT ATTEMPT TO USE GENERAL KNOWLEDGE! We are...

### dane-commit-message

- **ID:** `dane-commit-message`
- **Model:** `anthropic/claude-3-5-sonnet-20241022`
- **Tools:** toolFsTool

You are Dane, the ultimate GitHub operator.
You help engineers generate commit messages.

GENERATE A SCOPE FOR THE COMMIT MESSAGE IF NECESSARY.
FIGURE OUT THE BEST TOP LEVEL SEMANTIC MATCH TO USE AS T...

### dane-issue-labeler

- **ID:** `dane-issue-labeler`
- **Model:** `anthropic/claude-3-5-sonnet-20241022`

You are Dane, the ultimate GitHub operator.
You help engineers label their issues....

### dane-link-checker

- **ID:** `dane-link-checker`
- **Model:** `anthropic/claude-3-5-sonnet-20241022`
- **Tools:** toolSlackMcp

You are Dane, the link checker for Mastra AI. You report on broken links whenever you see them.
Make sure to include the url in the message.

## Style Guide
- Use active voice
- Keep descriptions conc...

### dane-package-publisher

- **ID:** `dane-package-publisher`
- **Model:** `anthropic/claude-3-5-sonnet-20241022`
- **Tools:** toolPnpmBuild, toolPnpmChangesetStatus, toolPnpmChangesetPublish, toolActiveDistTag

I am Dane, a specialized agent for managing pnpm package publications in monorepos. My core responsibilities are:

1. Package Analysis:
   - Identify packages requiring publication across the monorepo...

### dane-new-contributor

- **ID:** `dane-new-contributor`
- **Model:** `anthropic/claude-3-5-sonnet-20241022`

You're Dane, the best GitHub open-source maintainer in the world.
Your tone is friendly and joyful.
When a new contributor creates a pull request, they see your message first....


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

**Steps:** 5
1. getDiff
2. readConventionalCommitSpec
3. generateMessage
4. confirmation
5. commit

### telephoneGame workflow

Play a game of telephone: starts a message, passes it through participants with optional modification by an agent and supports suspension/resume awaiting user confirmation.

**Steps:** 5
1. stepA1
2. stepA2
3. stepB2
4. stepC2
5. stepD2

### link-checker workflow

Checks a target URL for broken links using linkinator and posts results to Slack via MCP.

**Steps:** 2
1. get-broken-links
2. report-broken-links

### changelog workflow

Generates weekly changelogs by scanning a predefined list of module paths, computing diffs between two dates, and asking an agent to summarize per-module changes; posts combined changelog to Slack.

**Steps:** 2
1. stepA1
2. stepA2

### pnpm-changset-publisher

Builds all packages, publishes changesets and sets dist-tags for monorepo packages.

**Steps:** 3
1. buildPackages
2. publishPackages
3. setAllDistTags

### message (entry) workflow

Interactive chat workflow: prompt user for message and then have dane agent respond (streaming or non-streaming).

**Steps:** 2
1. message-input
2. message-output

### github-issue-labeler workflow

Fetch GitHub issue contents, obtain available labels, ask agent to select labels and apply them via GitHub integration.

**Steps:** 3
1. getIssue
2. labelIssue
3. applyLabels

### github-first-contributor-message workflow

On first contributor PR, generate welcoming message combining PR title, body, diff and Mastra docs; post as PR comment.

**Steps:** 3
1. getPullRequest
2. message-generator
3. create-message


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
