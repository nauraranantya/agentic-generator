import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { ChatOpenAI } from "@langchain/openai";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

async function writeEmail(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a email_assistant." +
        "\\nNode: writeEmail",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}
async function interrupt(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a email_assistant." +
        "\\nNode: interrupt",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}
async function rewriteEmail(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a email_assistant." +
        "\\nNode: rewriteEmail",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}
async function sendEmail(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a email_assistant." +
        "\\nNode: sendEmail",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("writeEmail", writeEmail)
  .addNode("interrupt", interrupt)
  .addNode("rewriteEmail", rewriteEmail)
  .addNode("sendEmail", sendEmail)
  .addEdge(START, "writeEmail")
  .addEdge("writeEmail", "interrupt")
  .addEdge("rewriteEmail", "interrupt")
  .addEdge("sendEmail", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
