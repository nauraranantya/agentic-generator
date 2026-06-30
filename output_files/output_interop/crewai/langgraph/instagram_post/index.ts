import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const CopyCrewAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: tool_browser_tools_scrape_and_summarize
const tool_browser_tools_scrape_and_summarize = tool(
  async () => {
    return "Result of tool_browser_tools_scrape_and_summarize";
  },
  {
    name: "tool_browser_tools_scrape_and_summarize",
    description: "Semantic purpose: Scrape a website and produce a long summary of its content or content chunks.
Input: full URL string (e.g., https://example.com).
Outputs: textual scrapped content and summaries (used as context for agents/tasks).
Configuration: requires a Browserless API key (SERPER/BROWSERLESS keys are present in Config entries).
Note: Implementation uses HTML partitioning into chunks and summary generation per chunk; we capture purpose and required config here.",
    schema: z.object({}),
  }
);
// Tool: tool_search_tools_search_internet
const tool_search_tools_search_internet = tool(
  async () => {
    return "Result of tool_search_tools_search_internet";
  },
  {
    name: "tool_search_tools_search_internet",
    description: "Semantic purpose: Search the Internet (generic web search) and return top organic results, title, link, snippet.
Input: query string.
Configuration: uses SERPER_API_KEY (search service) as an API key.",
    schema: z.object({}),
  }
);
// Tool: tool_search_tools_search_instagram
const tool_search_tools_search_instagram = tool(
  async () => {
    return "Result of tool_search_tools_search_instagram";
  },
  {
    name: "tool_search_tools_search_instagram",
    description: "Semantic purpose: Search Instagram via site-limited search (site:instagram.com) to find relevant posts.
Input: query string.
Configuration: uses SERPER_API_KEY (search service) as an API key.",
    schema: z.object({}),
  }
);



/**
 * Node: taskProductAnalysis
 * Agent: product_competitor_agent
 */
async function taskProductAnalysis(state: typeof CopyCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent backstory and role description for Lead Market Analyst" +
        "\\nNode: taskProductAnalysis",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskCompetitorAnalysis
 * Agent: product_competitor_agent
 */
async function taskCompetitorAnalysis(state: typeof CopyCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent backstory and role description for Lead Market Analyst" +
        "\\nNode: taskCompetitorAnalysis",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskCampaignDevelopment
 * Agent: strategy_planner_agent
 */
async function taskCampaignDevelopment(state: typeof CopyCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent backstory and role description for Chief Marketing Strategist" +
        "\\nNode: taskCampaignDevelopment",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskInstagramAdCopy
 * Agent: creative_content_creator_agent
 */
async function taskInstagramAdCopy(state: typeof CopyCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent backstory and role description for Creative Content Creator" +
        "\\nNode: taskInstagramAdCopy",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskTakePhotograph
 * Agent: senior_photographer_agent
 */
async function taskTakePhotograph(state: typeof CopyCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent backstory and role description for Senior Photographer" +
        "\\nNode: taskTakePhotograph",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskReviewPhoto
 * Agent: chief_creative_director_agent
 */
async function taskReviewPhoto(state: typeof CopyCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent backstory and role description for Chief Creative Director" +
        "\\nNode: taskReviewPhoto",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(CopyCrewAnnotation)
  .addNode("taskProductAnalysis", taskProductAnalysis)
  .addNode("taskCompetitorAnalysis", taskCompetitorAnalysis)
  .addNode("taskCampaignDevelopment", taskCampaignDevelopment)
  .addNode("taskInstagramAdCopy", taskInstagramAdCopy)
  .addNode("taskTakePhotograph", taskTakePhotograph)
  .addNode("taskReviewPhoto", taskReviewPhoto)
  .addEdge(START, "taskProductAnalysis")
  .addEdge("taskProductAnalysis", "taskCompetitorAnalysis")
  .addEdge("taskCompetitorAnalysis", "taskCampaignDevelopment")
  .addEdge("taskCampaignDevelopment", "taskInstagramAdCopy")
  .addEdge("taskInstagramAdCopy", "taskTakePhotograph")
  .addEdge("taskTakePhotograph", "taskReviewPhoto")
  .addEdge("taskReviewPhoto", END)
;

export const graph = workflow.compile();
graph.name = "CopyCrew";
// Workflow: wp_copy_crew
// Workflow: Workflow Pattern - Copy Crew
// Workflow: wp_image_crew
// Workflow: Workflow Pattern - Image Crew
