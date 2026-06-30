import { ChatAnthropic } from "@langchain/anthropic";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const MastraDeploymentBirdCheckerAnnotation = Annotation.Root({
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
    description: "Gets a random image from Unsplash based on the selected option (query enum). Declared as a tool in src/mastra/tools.",
    schema: z.object({}),
  }
);



/**
 * Node: getRandomImageTask
 * Agent: bird_agent
 */
async function getRandomImageTask(state: typeof MastraDeploymentBirdCheckerAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-haiku-20240307" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "agent instructions (default context for agent)" +
        "\nNode: getRandomImageTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: analyzeImageTask
 * Agent: bird_agent
 */
async function analyzeImageTask(state: typeof MastraDeploymentBirdCheckerAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-haiku-20240307" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "agent instructions (default context for agent)" +
        "\nNode: analyzeImageTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(MastraDeploymentBirdCheckerAnnotation)
  .addNode("getRandomImageTask", getRandomImageTask)
  .addNode("analyzeImageTask", analyzeImageTask)
  .addEdge(START, "getRandomImageTask")
  .addEdge("getRandomImageTask", "analyzeImageTask")
;

export const graph = workflow.compile();
graph.name = "MastraDeploymentBirdChecker";
// Workflow: bird_checker_workflow
// Workflow: Bird Checker Workflow Pattern
