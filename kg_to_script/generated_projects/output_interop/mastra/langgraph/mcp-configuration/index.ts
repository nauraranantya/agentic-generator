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

// Tool: stock_price_tool
const stock_price_tool = tool(
  async () => {
    return "Result of stock_price_tool";
  },
  {
    name: "stock_price_tool",
    description: "Tool exposing a single capability 'getStockPrice'. It fetches the last day's closing stock price for a given symbol from https://mastra-stock-data.vercel.app/api/stock-data?symbol=<SYMBOL>. Returns JSON text object: { "symbol": "<SYMBOL>", "currentPrice": <price> } as tool content. The tool is made available to the agent via a toolset listing (server process that exposes tools). The server process also includes an environment variable FAKE_CREDS used during server launch; captured in tool config.",
    schema: z.object({}),
  }
);
// Tool: weather_tool
const weather_tool = tool(
  async () => {
    return "Result of weather_tool";
  },
  {
    name: "weather_tool",
    description: "Tool exposing 'getWeather' capability. It resolves a location via a geocoding service, calls an external weather API (open-meteo) to get current conditions and returns a JSON structure containing temperature, feelsLike, humidity, windSpeed, windGust, conditions, and location. This tool is exposed over an SSE-backed server endpoint at http://localhost:8080/sse in the example environment. The tool expects a 'location' string (city name).",
    schema: z.object({}),
  }
);



/**
 * Node: userRequestTask
 * Agent: stock_weather_agent
 */
async function userRequestTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level system instructions for independent operation (agent behavior and role)." +
        "\nNode: userRequestTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: getWeatherTask
 * Agent: stock_weather_agent
 */
async function getWeatherTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level system instructions for independent operation (agent behavior and role)." +
        "\nNode: getWeatherTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: getStockPriceTask
 * Agent: stock_weather_agent
 */
async function getStockPriceTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level system instructions for independent operation (agent behavior and role)." +
        "\nNode: getStockPriceTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("userRequestTask", userRequestTask)
  .addNode("getWeatherTask", getWeatherTask)
  .addNode("getStockPriceTask", getStockPriceTask)
  .addEdge(START, "userRequestTask")
  .addEdge("getWeatherTask", "getStockPriceTask")
  .addEdge("userRequestTask", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: stock_weather_workflow
