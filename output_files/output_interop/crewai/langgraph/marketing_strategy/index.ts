import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const MarketingPostsCrewTeamAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: serper_dev_tool
const serper_dev_tool = tool(
  async () => {
    return "Result of serper_dev_tool";
  },
  {
    name: "serper_dev_tool",
    description: "Third-party web search / SERP tool used by agents for lookups. Instantiated in code as SerperDevTool().",
    schema: z.object({}),
  }
);
// Tool: scrape_website_tool
const scrape_website_tool = tool(
  async () => {
    return "Result of scrape_website_tool";
  },
  {
    name: "scrape_website_tool",
    description: "Tool for scraping website contents; used by agents to gather site-specific information. Instantiated in code as ScrapeWebsiteTool().",
    schema: z.object({}),
  }
);



/**
 * Node: researchTask
 * Agent: lead_market_analyst
 */
async function researchTask(state: typeof MarketingPostsCrewTeamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Role and backstory for agent" +
        "\\nNode: researchTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: projectUnderstandingTask
 * Agent: chief_marketing_strategist
 */
async function projectUnderstandingTask(state: typeof MarketingPostsCrewTeamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Role and backstory for agent" +
        "\\nNode: projectUnderstandingTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: marketingStrategyTask
 * Agent: chief_marketing_strategist
 */
async function marketingStrategyTask(state: typeof MarketingPostsCrewTeamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Role and backstory for agent" +
        "\\nNode: marketingStrategyTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: campaignIdeaTask
 * Agent: creative_content_creator
 */
async function campaignIdeaTask(state: typeof MarketingPostsCrewTeamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Role and backstory for agent" +
        "\\nNode: campaignIdeaTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: copyCreationTask
 * Agent: creative_content_creator
 */
async function copyCreationTask(state: typeof MarketingPostsCrewTeamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Role and backstory for agent" +
        "\\nNode: copyCreationTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(MarketingPostsCrewTeamAnnotation)
  .addNode("researchTask", researchTask)
  .addNode("projectUnderstandingTask", projectUnderstandingTask)
  .addNode("marketingStrategyTask", marketingStrategyTask)
  .addNode("campaignIdeaTask", campaignIdeaTask)
  .addNode("copyCreationTask", copyCreationTask)
  .addEdge(START, "researchTask")
  .addEdge("researchTask", "projectUnderstandingTask")
  .addEdge("projectUnderstandingTask", "marketingStrategyTask")
  .addEdge("marketingStrategyTask", "campaignIdeaTask")
  .addEdge("campaignIdeaTask", "copyCreationTask")
  .addEdge("copyCreationTask", END)
;

export const graph = workflow.compile();
graph.name = "MarketingPostsCrewTeam";
// Workflow: marketing_posts_workflow
// Workflow: MarketingPosts Workflow Pattern
