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

// Tool: get_weather_tool
const get_weather_tool = tool(
  async () => {
    return "Result of get_weather_tool";
  },
  {
    name: "get_weather_tool",
    description: "Get current weather for a location",
    schema: z.object({}),
  }
);



/**
 * Node: fetchCurrentWeather
 * Agent: weather_agent
 */
async function fetchCurrentWeather(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Weather assistant." +
        "\nNode: fetchCurrentWeather",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: weatherAgentParticipationPlaceholder
 * Agent: weather_agent
 */
async function weatherAgentParticipationPlaceholder(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Weather assistant." +
        "\nNode: weatherAgentParticipationPlaceholder",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("fetchCurrentWeather", fetchCurrentWeather)
  .addNode("weatherAgentParticipationPlaceholder", weatherAgentParticipationPlaceholder)
  .addEdge(START, "fetchCurrentWeather")
  .addEdge("fetchCurrentWeather", "weatherAgentParticipationPlaceholder")
  .addEdge("weatherAgentParticipationPlaceholder", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
