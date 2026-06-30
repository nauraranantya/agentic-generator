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

// Tool: console_tool
const console_tool = tool(
  async () => {
    return "Result of console_tool";
  },
  {
    name: "console_tool",
    description: "Represents the runtime logging facility used by the step (the source prints to console via console.log). Modeled as a Tool to indicate the step uses an execution tool.",
    schema: z.object({}),
  }
);



/**
 * Node: taskLogCatName
 * Agent: cat_one
 */
async function taskLogCatName(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Default agent-level instructions to guide behavior when the agent is asked about cat species. This prompt is intended to be used by the agent as its core persona/instructions." +
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
// Workflow: log_cat_workflow_pattern
// Workflow: legacy_log_cat_workflow_pattern
