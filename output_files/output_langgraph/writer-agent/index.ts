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

// Tool: draft_text_document_tool
const draft_text_document_tool = tool(
  async () => {
    return "Result of draft_text_document_tool";
  },
  {
    name: "draft_text_document_tool",
    description: "Prepare a text document for the user with a short title and short description for browsing purposes. Can be also used when creating a new version of the document.",
    schema: z.object({}),
  }
);



/**
 * Node: prepareTask
 * Agent: writer_annotation_agent_uuid_1
 */
async function prepareTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-latest" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a annotation-driven writer." +
        "\\nNode: prepareTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: writeTask
 * Agent: writer_annotation_agent_uuid_1
 */
async function writeTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-latest" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a annotation-driven writer." +
        "\\nNode: writeTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: suggestionsTask
 * Agent: writer_annotation_agent_uuid_1
 */
async function suggestionsTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-latest" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a annotation-driven writer." +
        "\\nNode: suggestionsTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("prepareTask", prepareTask)
  .addNode("writeTask", writeTask)
  .addNode("suggestionsTask", suggestionsTask)
  .addEdge(START, "prepareTask")
  .addEdge("prepareTask", "writeTask")
  .addEdge("writeTask", "suggestionsTask")
  .addEdge("suggestionsTask", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
