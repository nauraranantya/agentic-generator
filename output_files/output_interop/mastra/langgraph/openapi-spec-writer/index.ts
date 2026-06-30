import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const MastraSystemAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: site_crawl_tool
const site_crawl_tool = tool(
  async () => {
    return "Result of site_crawl_tool";
  },
  {
    name: "site_crawl_tool",
    description: "Crawl a website and extract the markdown content",
    schema: z.object({}),
  }
);
// Tool: firecrawl_integration
const firecrawl_integration = tool(
  async () => {
    return "Result of firecrawl_integration";
  },
  {
    name: "firecrawl_integration",
    description: "Integration client used to crawl websites (Firecrawl API key supplied at runtime).",
    schema: z.object({}),
  }
);
// Tool: generate_spec_tool
const generate_spec_tool = tool(
  async () => {
    return "Result of generate_spec_tool";
  },
  {
    name: "generate_spec_tool",
    description: "Generate an OpenAPI spec from crawled website markdown; uses the OpenAPI agent to convert pages and merge them.",
    schema: z.object({}),
  }
);
// Tool: add_to_git_hub_tool
const add_to_git_hub_tool = tool(
  async () => {
    return "Result of add_to_git_hub_tool";
  },
  {
    name: "add_to_git_hub_tool",
    description: "Commit the spec to GitHub: formats YAML via the agent, creates branch, commits files and opens a pull request.",
    schema: z.object({}),
  }
);
// Tool: git_hub_integration
const git_hub_integration = tool(
  async () => {
    return "Result of git_hub_integration";
  },
  {
    name: "git_hub_integration",
    description: "GitHub integration client that performs git ref, file write and pull request operations (requires PERSONAL_ACCESS_TOKEN).",
    schema: z.object({}),
  }
);



/**
 * Node: siteCrawlSyncStepTask
 * Agent: openapi_spec_gen_agent
 */
async function siteCrawlSyncStepTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-3.5-turbo" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a OpenAPI spec writer agent." +
        "\\nNode: siteCrawlSyncStepTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: generateSpecTask
 * Agent: openapi_spec_gen_agent
 */
async function generateSpecTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-3.5-turbo" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a OpenAPI spec writer agent." +
        "\\nNode: generateSpecTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: addToGithubTask
 * Agent: openapi_spec_gen_agent
 */
async function addToGithubTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-3.5-turbo" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a OpenAPI spec writer agent." +
        "\\nNode: addToGithubTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(MastraSystemAnnotation)
  .addNode("siteCrawlSyncStepTask", siteCrawlSyncStepTask)
  .addNode("generateSpecTask", generateSpecTask)
  .addNode("addToGithubTask", addToGithubTask)
  .addEdge(START, "siteCrawlSyncStepTask")
  .addEdge("siteCrawlSyncStepTask", "generateSpecTask")
  .addEdge("generateSpecTask", "addToGithubTask")
  .addEdge("addToGithubTask", END)
;

export const graph = workflow.compile();
graph.name = "MastraSystem";
// Workflow: open_api_spec_gen_workflow_pattern
// Workflow: openApiSpecGenWorkflow
// Workflow: make_pr_workflow_pattern
// Workflow: makePRToMastra
