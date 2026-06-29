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

// Tool: tool_extract
const tool_extract = tool(
  async () => {
    return "Result of tool_extract";
  },
  {
    name: "tool_extract",
    description: "Tool name: "extract"
Purpose: Extract TripDetails from conversation history. Bound to the agent's LLM.
Schema (Zod, represented informally):
{
  location: string (describe: The location to plan the trip for. Can be a city, state, or country.),
  startDate: string (optional, describe: The start date of the trip. YYYY-MM-DD),
  endDate: string (optional, describe: The end date of the trip. YYYY-MM-DD),
  numberOfGuests: number (describe: The number of guests. Defaults to 2 if unspecified.)
}
Behavior: the tool returns only fields specified by the user; do not make up values. If location is missing, a clarification message should be generated requesting the location.",
    schema: z.object({}),
  }
);
// Tool: tool_classify
const tool_classify = tool(
  async () => {
    return "Result of tool_classify";
  },
  {
    name: "tool_classify",
    description: "Tool name: "classify"
Purpose: Classify whether trip details remain relevant to the user's most recent request.
Schema:
{
  isRelevant: boolean (describe: Whether the trip details are still relevant to the user's request.)
}
Notes: When invoked, tool_choice is set to "classify" in the implementation.",
    schema: z.object({}),
  }
);
// Tool: tool_list_accommodations
const tool_list_accommodations = tool(
  async () => {
    return "Result of tool_list_accommodations";
  },
  {
    name: "tool_list_accommodations",
    description: "Tool name: "list-accommodations"
Purpose: A tool to list accommodations for the user. Implementation populates an accommodations list (id, name, price, rating, city, image) using a data generator.
Schema: {} (no input schema fields required in the implementation).
Produces: An accommodations list resource used to populate UI.",
    schema: z.object({}),
  }
);
// Tool: tool_list_restaurants
const tool_list_restaurants = tool(
  async () => {
    return "Result of tool_list_restaurants";
  },
  {
    name: "tool_list_restaurants",
    description: "Tool name: "list-restaurants"
Purpose: A tool to list restaurants for the user. Implementation uses trip details to produce a restaurants list.
Schema: {}.
Produces: A restaurants list resource used to populate UI.",
    schema: z.object({}),
  }
);



/**
 * Node: taskExtraction
 * Agent: trip_planner_agent
 */
async function taskExtraction(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant / trip-planner." +
        "\nNode: taskExtraction",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskClassify
 * Agent: trip_planner_agent
 */
async function taskClassify(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant / trip-planner." +
        "\nNode: taskClassify",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskCallTools
 * Agent: trip_planner_agent
 */
async function taskCallTools(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant / trip-planner." +
        "\nNode: taskCallTools",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("taskExtraction", taskExtraction)
  .addNode("taskClassify", taskClassify)
  .addNode("taskCallTools", taskCallTools)
  .addEdge(START, "taskExtraction")
  .addEdge("taskExtraction", "taskCallTools")
  .addEdge("taskClassify", "taskExtraction")
  .addEdge("taskClassify", "taskCallTools")
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
