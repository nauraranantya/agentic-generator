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

// Tool: write_email_tool
const write_email_tool = tool(
  async () => {
    return "Result of write_email_tool";
  },
  {
    name: "write_email_tool",
    description: "Tool binding used by the LLM to produce structured email objects. Description: "Write an email based on the conversation history".",
    schema: z.object({}),
  }
);



/**
 * Node: writeEmailGenerateDraft
 * Agent: email_assistant_agent
 */
async function writeEmailGenerateDraft(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a email_assistant." +
        "\nNode: writeEmailGenerateDraft",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: ignore
 * Agent: email_assistant_agent
 */
async function ignore(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a email_assistant." +
        "\nNode: ignore",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: rewriteEmailApplyUserSRequestedChanges
 * Agent: email_assistant_agent
 */
async function rewriteEmailApplyUserSRequestedChanges(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a email_assistant." +
        "\nNode: rewriteEmailApplyUserSRequestedChanges",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: sendEmailFinalizeSend
 * Agent: email_assistant_agent
 */
async function sendEmailFinalizeSend(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a email_assistant." +
        "\nNode: sendEmailFinalizeSend",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("writeEmailGenerateDraft", writeEmailGenerateDraft)
  .addNode("ignore", ignore)
  .addNode("rewriteEmailApplyUserSRequestedChanges", rewriteEmailApplyUserSRequestedChanges)
  .addNode("sendEmailFinalizeSend", sendEmailFinalizeSend)
  .addEdge(START, "writeEmailGenerateDraft")
  .addEdge("writeEmailGenerateDraft", "ignore")
  .addEdge("ignore", "sendEmailFinalizeSend")
  .addEdge("ignore", "rewriteEmailApplyUserSRequestedChanges")
  .addEdge("rewriteEmailApplyUserSRequestedChanges", "ignore")
  .addEdge("sendEmailFinalizeSend", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
