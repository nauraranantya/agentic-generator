import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";


const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

async function interrupt(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a email_assistant." +
        "\nNode: interrupt",
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
        "\nNode: rewriteEmail",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}


const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("interrupt", interrupt)
  .addNode("rewriteEmail", rewriteEmail)
  .addEdge("writeEmail", "interrupt")
  .addEdge("interrupt", "sendEmail")
  .addEdge("interrupt", "rewriteEmail")
  .addEdge("rewriteEmail", "interrupt")
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
