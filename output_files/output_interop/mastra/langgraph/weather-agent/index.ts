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

// Tool: weather_tool
const weather_tool = tool(
  async () => {
    return "Result of weather_tool";
  },
  {
    name: "weather_tool",
    description: "Tool to get current weather for a location. Wraps geocoding and open-meteo APIs and returns a simplified weather object (temperature, feelsLike, humidity, windSpeed, windGust, conditions, location).",
    schema: z.object({}),
  }
);



/**
 * Node: fetchWeatherTask
 * Agent: weather_agent
 */
async function fetchWeatherTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a weather assistant." +
        "\\nNode: fetchWeatherTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: planActivities
 * Agent: weather_agent
 */
async function planActivities(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a weather assistant." +
        "\\nNode: planActivities",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: weatherToolCallTask
 * Agent: weather_agent
 */
async function weatherToolCallTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a weather assistant." +
        "\\nNode: weatherToolCallTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: mapForecastToPromptTask
 * Agent: weather_agent
 */
async function mapForecastToPromptTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a weather assistant." +
        "\\nNode: mapForecastToPromptTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: explainWeatherTask
 * Agent: weather_agent
 */
async function explainWeatherTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a weather assistant." +
        "\\nNode: explainWeatherTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(MastraSystemAnnotation)
  .addNode("fetchWeatherTask", fetchWeatherTask)
  .addNode("planActivities", planActivities)
  .addNode("weatherToolCallTask", weatherToolCallTask)
  .addNode("mapForecastToPromptTask", mapForecastToPromptTask)
  .addNode("explainWeatherTask", explainWeatherTask)
  .addEdge(START, "fetchWeatherTask")
  .addEdge("fetchWeatherTask", "planActivities")
  .addEdge("planActivities", "weatherToolCallTask")
  .addEdge("weatherToolCallTask", "mapForecastToPromptTask")
  .addEdge("mapForecastToPromptTask", "explainWeatherTask")
  .addEdge("explainWeatherTask", END)
;

export const graph = workflow.compile();
graph.name = "MastraSystem";
// Workflow: wf_weather_workflow
// Workflow: weather-workflow
// Workflow: wf_weather_workflow_with_tool_and_agent
// Workflow: weather-workflow-with-tool-and-agent
