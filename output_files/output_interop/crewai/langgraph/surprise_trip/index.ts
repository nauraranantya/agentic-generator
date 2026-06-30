import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const SurpriseTravelCrewAnnotation = Annotation.Root({
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
    description: "Search / web tools used to query the web (as configured in the source crew).",
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
    description: "Tool to scrape website content; used by agents for gathering reviews and details.",
    schema: z.object({}),
  }
);
// Tool: my_custom_tool
const my_custom_tool = tool(
  async () => {
    return "Result of my_custom_tool";
  },
  {
    name: "my_custom_tool",
    description: "Example custom tool present in source (tools/custom_tool.py). This example tool is included in the repository but commented-out in crew agent configuration and not used by default.",
    schema: z.object({}),
  }
);



/**
 * Node: personalizedActivityPlanningTask
 * Agent: personalized_activity_planner
 */
async function personalizedActivityPlanningTask(state: typeof SurpriseTravelCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Use internet search tools and recommendation engines to gather information; produce day-by-day activities with name, location, description and suitability rationale." +
        "\nNode: personalizedActivityPlanningTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: restaurantScenicLocationScoutTask
 * Agent: restaurant_scout
 */
async function restaurantScenicLocationScoutTask(state: typeof SurpriseTravelCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Use internet search tools, restaurant review sites, and travel guides to find restaurants and scenic locations aligned with traveler preferences." +
        "\nNode: restaurantScenicLocationScoutTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: itineraryCompilationTask
 * Agent: itinerary_compiler
 */
async function itineraryCompilationTask(state: typeof SurpriseTravelCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Compile all researched information into a comprehensive day-by-day itinerary for the trip; ensure integration of flights, hotel information, activities, and restaurants. Use text formatting and document creation tools." +
        "\nNode: itineraryCompilationTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(SurpriseTravelCrewAnnotation)
  .addNode("personalizedActivityPlanningTask", personalizedActivityPlanningTask)
  .addNode("restaurantScenicLocationScoutTask", restaurantScenicLocationScoutTask)
  .addNode("itineraryCompilationTask", itineraryCompilationTask)
  .addEdge(START, "personalizedActivityPlanningTask")
  .addEdge("personalizedActivityPlanningTask", "restaurantScenicLocationScoutTask")
  .addEdge("restaurantScenicLocationScoutTask", "itineraryCompilationTask")
  .addEdge("itineraryCompilationTask", END)
;

export const graph = workflow.compile();
graph.name = "SurpriseTravelCrew";
// Workflow: surprise_travel_workflow
// Workflow: SurpriseTravel Sequential Workflow
