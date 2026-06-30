import { ChatAnthropic } from "@langchain/anthropic";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: get_random_image_tool
const get_random_image_tool = tool(
  async () => {
    return "Result of get_random_image_tool";
  },
  {
    name: "get_random_image_tool",
    description: "Tool that queries Unsplash and returns a single image object selected from search results. Implemented in the code using a GET to https://api.unsplash.com/search/photos with a query param and optional paging/randomization.",
    schema: z.object({}),
  }
);



/**
 * Node: fetchRandomImageTask
 * Agent: bird_checker
 */
async function fetchRandomImageTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-haiku-20240307" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent instruction and purpose" +
        "\nNode: fetchRandomImageTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: analyzeImageAndProduceBirdMetadata
 * Agent: bird_checker
 */
async function analyzeImageAndProduceBirdMetadata(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-haiku-20240307" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent instruction and purpose" +
        "\nNode: analyzeImageAndProduceBirdMetadata",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("fetchRandomImageTask", fetchRandomImageTask)
  .addNode("analyzeImageAndProduceBirdMetadata", analyzeImageAndProduceBirdMetadata)
  .addEdge(START, "fetchRandomImageTask")
  .addEdge("fetchRandomImageTask", "analyzeImageAndProduceBirdMetadata")
  .addEdge("analyzeImageAndProduceBirdMetadata", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: bird_checker_workflow
// Workflow: Bird Checker workflow pattern
