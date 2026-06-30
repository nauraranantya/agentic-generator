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

// Tool: get_random_image_tool
const get_random_image_tool = tool(
  async () => {
    return "Result of get_random_image_tool";
  },
  {
    name: "get_random_image_tool",
    description: "Gets a random image from Unsplash based on selected query option. Random page selection and order_by ('relevant' or 'latest') logic is applied at runtime.",
    schema: z.object({}),
  }
);



/**
 * Node: taskFetchRandomImage
 * Agent: bird_checker
 */
async function taskFetchRandomImage(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a image-analyst." +
        "\nNode: taskFetchRandomImage",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskAnalyzeImage
 * Agent: bird_checker
 */
async function taskAnalyzeImage(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a image-analyst." +
        "\nNode: taskAnalyzeImage",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("taskFetchRandomImage", taskFetchRandomImage)
  .addNode("taskAnalyzeImage", taskAnalyzeImage)
  .addEdge(START, "taskFetchRandomImage")
  .addEdge("taskFetchRandomImage", "taskAnalyzeImage")
  .addEdge("taskAnalyzeImage", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: image_metadata_workflow
