import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { ChatOpenAI } from "@langchain/openai";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

async function stepFindStore(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "claude-3-5-sonnet-latest" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "General system role description used by both nodes as the system message." +
        "\\nNode: stepFindStore",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}
async function stepOrderPizza(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "claude-3-5-sonnet-latest" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "General system role description used by both nodes as the system message." +
        "\\nNode: stepOrderPizza",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("stepFindStore", stepFindStore)
  .addNode("stepOrderPizza", stepOrderPizza)
  .addEdge(START, "stepFindStore")
  .addEdge("stepFindStore", "stepOrderPizza")
  .addEdge("stepOrderPizza", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
