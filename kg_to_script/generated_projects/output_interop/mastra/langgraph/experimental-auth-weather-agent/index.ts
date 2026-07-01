import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const MastraserversystemAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: weather_tool
const weather_tool = tool(
  async () => {
    return "Result of weather_tool";
  },
  {
    name: "weather_tool",
    description: "Get current weather for a location.

Behavior summary:
- Input: { location: string } (city name)
- Execution:
  1. Call geocoding API to resolve location -> latitude, longitude, name.
  2. Call weather API with latitude & longitude to get current and hourly weather.
  3. Map numeric weather_code to human-readable condition (mapping preserved in description).
  4. Return normalized object with keys: temperature, feelsLike, humidity, windSpeed, windGust, conditions, location.
- Errors: throws when location not found.",
    schema: z.object({}),
  }
);



/**
 * Node: fetchWeather
 * Agent: weather_agent
 */
async function fetchWeather(state: typeof MastraserversystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Weather Assistant." +
        "\\nNode: fetchWeather",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: planActivities
 * Agent: weather_agent
 */
async function planActivities(state: typeof MastraserversystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Weather Assistant." +
        "\\nNode: planActivities",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(MastraserversystemAnnotation)
  .addNode("fetchWeather", fetchWeather)
  .addNode("planActivities", planActivities)
  .addEdge(START, "fetchWeather")
  .addEdge("fetchWeather", "planActivities")
  .addEdge("planActivities", END)
;

export const graph = workflow.compile();
graph.name = "Mastraserversystem";
// Workflow: weather_workflow
// Workflow: weather-workflow
