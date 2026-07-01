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
    description: "Gets a random image from Unsplash based on the selected option",
    schema: z.object({}),
  }
);



/**
 * Node: getRandomImageTask
 * Agent: bird_checker
 */
async function getRandomImageTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a bird-checker." +
        "\nNode: getRandomImageTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: imageMetadataTask
 * Agent: bird_checker
 */
async function imageMetadataTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a bird-checker." +
        "\nNode: imageMetadataTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("getRandomImageTask", getRandomImageTask)
  .addNode("imageMetadataTask", imageMetadataTask)
  .addEdge(START, "getRandomImageTask")
  .addEdge("getRandomImageTask", "imageMetadataTask")
  .addEdge("imageMetadataTask", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: bird_check_workflow
