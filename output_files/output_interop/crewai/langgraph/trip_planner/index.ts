import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: search_tools
const search_tools = tool(
  async () => {
    return "Result of search_tools";
  },
  {
    name: "search_tools",
    description: "Toolset providing search_internet(query) which posts to Serper API and returns top organic results. Top results are returned in a formatted text with Title/Link/Snippet.",
    schema: z.object({}),
  }
);
// Tool: browser_tools
const browser_tools = tool(
  async () => {
    return "Result of browser_tools";
  },
  {
    name: "browser_tools",
    description: "Scrape website content using Browserless content API; partitions HTML and produces chunk summaries by running an internal summarization agent.",
    schema: z.object({}),
  }
);
// Tool: calculator_tools
const calculator_tools = tool(
  async () => {
    return "Result of calculator_tools";
  },
  {
    name: "calculator_tools",
    description: "Make a calculation(operation) evaluates basic arithmetic expressions safely using AST validation and a whitelist of allowed tokens.",
    schema: z.object({}),
  }
);



/**
 * Node: identifyTask
 * Agent: city_selection_agent
 */
async function identifyTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Role: City Selection Expert; purpose: select the best city based on weather, season, and prices." +
        "\\nNode: identifyTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: gatherTask
 * Agent: local_expert_agent
 */
async function gatherTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Role: Local Expert; purpose: compile an in-depth city guide with hidden gems and local insights." +
        "\\nNode: gatherTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: planTask
 * Agent: travel_concierge_agent
 */
async function planTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Role: Travel Concierge; purpose: produce a full 7-day itinerary, budget breakdown and packing suggestions." +
        "\\nNode: planTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("identifyTask", identifyTask)
  .addNode("gatherTask", gatherTask)
  .addNode("planTask", planTask)
  .addEdge(START, "identifyTask")
  .addEdge("identifyTask", "gatherTask")
  .addEdge("gatherTask", "planTask")
  .addEdge("planTask", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: trip_planning_pattern
