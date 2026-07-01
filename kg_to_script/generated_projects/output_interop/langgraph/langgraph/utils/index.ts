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

// Tool: capitalize_tool
const capitalize_tool = tool(
  async () => {
    return "Result of capitalize_tool";
  },
  {
    name: "capitalize_tool",
    description: "Tool grouping for two capitalization utilities. Implements two conceptual capabilities: (1) capitalizeSentence: capitalizes the first letter of each word in a sentence by splitting on spaces and transforming tokens; (2) capitalize: capitalizes the first letter of a string. Implementation notes: these utilities treat the delimiter as a space character; they operate on Unicode strings in a straightforward per-character manner. They are pure string-processing utilities with no external dependencies in their conceptual model.",
    schema: z.object({}),
  }
);
// Tool: format_messages_tool
const format_messages_tool = tool(
  async () => {
    return "Result of format_messages_tool";
  },
  {
    name: "format_messages_tool",
    description: "Tool that serializes an ordered collection of messages into a formatted string. Conceptual behavior: iterates over messages, determines role via message.getType(), stringifies content if not a string (conceptually using JSON serialization), wraps content in role-based tags with index attribute, and concatenates the blocks with newlines. This tool expects each message to expose a 'getType' semantics and a content payload that is either string or serializable.",
    schema: z.object({}),
  }
);



/**
 * Node: capitalizeSentenceTask
 * Agent: defaultAgent
 */
async function capitalizeSentenceTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a helpful assistant." +
        "\nNode: capitalizeSentenceTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: capitalizeTask
 * Agent: defaultAgent
 */
async function capitalizeTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a helpful assistant." +
        "\nNode: capitalizeTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: formatMessagesTask
 * Agent: defaultAgent
 */
async function formatMessagesTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a helpful assistant." +
        "\nNode: formatMessagesTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("capitalizeSentenceTask", capitalizeSentenceTask)
  .addNode("capitalizeTask", capitalizeTask)
  .addNode("formatMessagesTask", formatMessagesTask)
  .addEdge(START, "capitalizeSentenceTask")
  .addEdge("capitalizeSentenceTask", "capitalizeTask")
  .addEdge("capitalizeTask", "formatMessagesTask")
  .addEdge("formatMessagesTask", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: text_utilities_workflow_pattern
