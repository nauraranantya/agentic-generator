import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const TravelAISystemMastraexampleappAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: search_flights_tool
const search_flights_tool = tool(
  async () => {
    return "Result of search_flights_tool";
  },
  {
    name: "search_flights_tool",
    description: "Fetches flight information for a given date range, origin and destination. Origin and Destination are Airport codes like DFW.AIRPORT or SEA.AIRPORT",
    schema: z.object({}),
  }
);
// Tool: search_hotels_tool
const search_hotels_tool = tool(
  async () => {
    return "Result of search_hotels_tool";
  },
  {
    name: "search_hotels_tool",
    description: "Searches for hotels in a specified location. Destination is a cityId like 20015732 for 20015733",
    schema: z.object({}),
  }
);
// Tool: search_attractions_tool
const search_attractions_tool = tool(
  async () => {
    return "Result of search_attractions_tool";
  },
  {
    name: "search_attractions_tool",
    description: "Searches for attractions in a specified location. Destination is a cityId like 20015732 for 20015733",
    schema: z.object({}),
  }
);
// Tool: search_airbnb_location_tool
const search_airbnb_location_tool = tool(
  async () => {
    return "Result of search_airbnb_location_tool";
  },
  {
    name: "search_airbnb_location_tool",
    description: "Searches for Airbnb places in a specified location. Place is a city name like New York, NY",
    schema: z.object({}),
  }
);
// Tool: search_airbnb_tool
const search_airbnb_tool = tool(
  async () => {
    return "Result of search_airbnb_tool";
  },
  {
    name: "search_airbnb_tool",
    description: "Searches for Airbnb in a specified location. Place is a cityId like 20015732 for 20015733",
    schema: z.object({}),
  }
);



/**
 * Node: findOutboundFlight
 * Agent: travel_agent
 */
async function findOutboundFlight(state: typeof TravelAISystemMastraexampleappAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level instruction used on agent initialization" +
        "\nNode: findOutboundFlight",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: findReturnFlight
 * Agent: travel_agent
 */
async function findReturnFlight(state: typeof TravelAISystemMastraexampleappAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level instruction used on agent initialization" +
        "\nNode: findReturnFlight",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: findAccommodationHotelOrAirbnb
 * Agent: travel_agent
 */
async function findAccommodationHotelOrAirbnb(state: typeof TravelAISystemMastraexampleappAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level instruction used on agent initialization" +
        "\nNode: findAccommodationHotelOrAirbnb",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: findAccommodationHotelOrAirbnb
 * Agent: travel_agent
 */
async function findAccommodationHotelOrAirbnb(state: typeof TravelAISystemMastraexampleappAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level instruction used on agent initialization" +
        "\nNode: findAccommodationHotelOrAirbnb",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: findAttractions
 * Agent: travel_agent
 */
async function findAttractions(state: typeof TravelAISystemMastraexampleappAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level instruction used on agent initialization" +
        "\nNode: findAttractions",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: syncCsvDataTask
 * Agent: travel_agent
 */
async function syncCsvDataTask(state: typeof TravelAISystemMastraexampleappAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level instruction used on agent initialization" +
        "\nNode: syncCsvDataTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(TravelAISystemMastraexampleappAnnotation)
  .addNode("findOutboundFlight", findOutboundFlight)
  .addNode("findReturnFlight", findReturnFlight)
  .addNode("findAccommodationHotelOrAirbnb", findAccommodationHotelOrAirbnb)
  .addNode("findAccommodationHotelOrAirbnb", findAccommodationHotelOrAirbnb)
  .addNode("findAttractions", findAttractions)
  .addNode("syncCsvDataTask", syncCsvDataTask)
  .addEdge(START, "findOutboundFlight")
  .addEdge("findOutboundFlight", "findReturnFlight")
  .addEdge("findReturnFlight", "findAccommodationHotelOrAirbnb")
  .addEdge("findAccommodationHotelOrAirbnb", "findAttractions")
  .addEdge("findAccommodationHotelOrAirbnb", "findAccommodationHotelOrAirbnb")
  .addEdge("findAccommodationHotelOrAirbnb", "findAccommodationHotelOrAirbnb")
  .addEdge("findAccommodationHotelOrAirbnb", "findAttractions")
  .addEdge("findAttractions", END)
  .addEdge("syncCsvDataTask", END)
;

export const graph = workflow.compile();
graph.name = "TravelAISystemMastraexampleapp";
// Workflow: travel_submission_workflow
// Workflow: travel-submission
// Workflow: airbnb_flow_pattern
// Workflow: airbnb-flow
// Workflow: sync_csv_workflow
// Workflow: syncCsvData
