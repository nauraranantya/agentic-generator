# MastraSystem

The system instance that contains agents, workflows, processors, MCP servers, and tools as configured in the source.

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
MastraSystem/
├── src/
│   └── mastra/
│       ├── index.ts           # Mastra instance + registrations
│       ├── agents/            # Agent definitions
│       │   └── chefAgent.ts
│       │   └── chefAgentResponses.ts
│       │   └── chefModelV2Agent.ts
│       │   └── dynamicAgent.ts
│       │   └── agentThatHarassesYou.ts
│       │   └── errorAgent.ts
│       │   └── networkAgent.ts
│       │   └── weatherAgent.ts
│       │   └── evalAgent.ts
│       ├── tools/             # Tool definitions
│       │   └── cookingTool.ts
│       │   └── weatherInfoTool.ts
│       │   └── calculatorTool.ts
│       │   └── fetchWeatherTool.ts
│       │   └── stringUtilsTool.ts
│       │   └── greetUserTool.ts
│       │   └── collectContactInfoTool.ts
│       └── workflows/         # Workflow definitions
│           └── recipeMakerWorkflow.ts
│           └── lessComplexWorkflow.ts
│           └── nestedWorkflow.ts
│           └── myWorkflowX.ts
├── package.json
├── tsconfig.json
└── .env.example
```

---

## 🤖 Agents

### LLM Agent

- **ID:** `chef-agent`
- **Model:** `openai/gpt-4o-mini`
- **Tools:** cookingTool, weatherInfoTool

Return a useful recipe given an ingredient and available tools/equipment....

### LLM Agent

- **ID:** `chef-agent-responses`
- **Model:** `openai/gpt-4o`
- **Tools:** cookingTool, weatherInfoTool

You are LLM Agent....

### LLM Agent

- **ID:** `chef-model-v2-agent`
- **Model:** `openai/gpt-4o-mini`
- **Tools:** cookingTool, weatherInfoTool

You are LLM Agent....

### LLM Agent

- **ID:** `dynamic-agent`
- **Model:** `openai/gpt-4o-mini`
- **Tools:** cookingTool

You are LLM Agent....

### LLM Agent

- **ID:** `agent-that-harasses-you`
- **Model:** `openai/gpt-4o`

You are LLM Agent....

### LLM Agent

- **ID:** `error-agent`
- **Model:** `openai/gpt-4o-mini`

You are LLM Agent....

### LLM Agent

- **ID:** `network-agent`
- **Model:** `openai/gpt-4o-mini`
- **Tools:** cookingTool, weatherInfoTool

You are LLM Agent....

### LLM Agent

- **ID:** `weather-agent`
- **Model:** `openai/gpt-4o-mini`
- **Tools:** weatherInfoTool

You are LLM Agent....

### LLM Agent

- **ID:** `eval-agent`
- **Model:** `openai/gpt-4o`
- **Tools:** weatherInfoTool

You are LLM Agent....


---

## 🔧 Tools

### cooking-tool

Tool ID: cooking-tool
    Description: Used to cook given an ingredient
    Input schema (zod): { ingredient: string }
    Behavior: Simulated long-running operation (sleep ~5000ms). Logs the ingredie...

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/cookingTool.ts`)

### weather-info

Tool ID: weather-info
    Description: Fetches the current weather information for a given city.
    Input schema: { city: string }
    Returns: an object with city, weather, temperature_celsius, temp...

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/weatherInfoTool.ts`)

### calculator

Tool ID: calculator
    Description: Performs basic arithmetic operations (add, subtract).
    Input schema: { num1: number, num2: number, operation: 'add'|'subtract' }
    Output: numeric result....

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/calculatorTool.ts`)

### fetchWeather

Tool ID: fetchWeather
    Description: Simulated forecast for a city. Uses a simple mapping from city to temperature string.
    Input schema: { city: string }
    Output: string describing weather (e...

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/fetchWeatherTool.ts`)

### stringUtils

Tool ID: stringUtils
    Description: Performs utility operations on strings (uppercase, reverse).
    Input schema: { text: string, action: 'uppercase'|'reverse' }
    Output: transformed text.
    N...

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/stringUtilsTool.ts`)

### greetUser

Tool ID: greetUser
    Description: Generates a personalized greeting.
    Input schema: { name: string }
    Output: greeting string 'Hello, {name}! Welcome to the MCP server.'...

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/greetUserTool.ts`)

### collectContactInfo

Tool ID: collectContactInfo
    Description: Collects user contact information through elicitation (interactive).
    Input schema: { reason?: string }
    Behavior:
      - Calls MCP elicitation sess...

**Status:** ⚠️ Implementation required (see TODO in `src/mastra/tools/collectContactInfoTool.ts`)


---

## 🔄 Workflows

### recipe-maker

Workflow: Returns a recipe based on an ingredient. Input: { ingredient: string }. Output: { result: string }.

**Steps:** 2
1. task:my-step
2. task:my-step-2

### lessComplexWorkflow

Complex workflow that:
      - Runs add-letter step
      - Executes two steps in parallel (add-letter-b, add-letter-c)
      - Maps parallel outputs to a single text
      - Branches on text length (short-text vs long-text)
      - Runs nestedTextProcessor
      - Loops with add-letter-with-count until text length >= 20
      - Presents suspend-resume step that requires user input
      - Runs final-step to produce final string '-ENDED'
    Input/Output: strings and counters as described by steps.

**Steps:** 9
1. task:add-letter
2. task:add-letter-b
3. task:add-letter-c
4. task:add-letter-with-count
5. task:suspend-resume
6. task:short-text
7. task:long-text
8. task:nested-text-processor
9. task:final-step

### data-processing

Nested workflow (id: data-processing). Steps: stepOne -> stepTwo -> stepThree -> stepFour.
    Purpose: numeric transformations (double, increment, triple, parity check).
    Input: { inputValue: number }, Output: { isEven: boolean }.

**Steps:** 4
1. task:stepOne
2. task:stepTwo
3. task:stepThree
4. task:stepFour

### my-workflow

Workflow that wraps the nested data-processing workflow.

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
