import { ChatAnthropic } from "@langchain/anthropic";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const MastraApplicationSystemAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: get_weather_tool
const get_weather_tool = tool(
  async () => {
    return "Result of get_weather_tool";
  },
  {
    name: "get_weather_tool",
    description: "Get current weather for a location. Tool accepts an input { location: string } and returns an object containing temperature, feelsLike, humidity, windSpeed, windGust, conditions, and location.",
    schema: z.object({}),
  }
);



/**
 * Node: fetchWeather
 * Agent: weather_agent
 */
async function fetchWeather(state: typeof MastraApplicationSystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a weather assistant." +
        "\\nNode: fetchWeather",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: planActivities
 * Agent: planning_agent
 */
async function planActivities(state: typeof MastraApplicationSystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\\nNode: planActivities",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(MastraApplicationSystemAnnotation)
  .addNode("fetchWeather", fetchWeather)
  .addNode("planActivities", planActivities)
  .addEdge(START, "fetchWeather")
  .addEdge("fetchWeather", "planActivities")
  .addEdge("planActivities", END)
;

export const graph = workflow.compile();
graph.name = "MastraApplicationSystem";
// Workflow: weather_workflow
// Workflow: weather-workflow
