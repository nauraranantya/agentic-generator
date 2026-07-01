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

// Tool: mastra_runtime
const mastra_runtime = tool(
  async () => {
    return "Result of mastra_runtime";
  },
  {
    name: "mastra_runtime",
    description: "Runtime engine that executes workflow step code (non-LLM execution).",
    schema: z.object({}),
  }
);



/**
 * Node: taskLogCatName
 * Agent: cat_one
 */
async function taskLogCatName(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a feline expert." +
        "\\nNode: taskLogCatName",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("taskLogCatName", taskLogCatName)
  .addEdge(START, "taskLogCatName")
  .addEdge("taskLogCatName", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: log_cat_workflow
