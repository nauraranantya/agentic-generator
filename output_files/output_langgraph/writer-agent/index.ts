import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { ChatOpenAI } from "@langchain/openai";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

async function prepare(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "claude-3-5-sonnet-latest" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a annotation-driven writer." +
        "\\nNode: prepare",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}
async function writer(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "claude-3-5-sonnet-latest" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a annotation-driven writer." +
        "\\nNode: writer",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}
async function suggestions(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "claude-3-5-sonnet-latest" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a annotation-driven writer." +
        "\\nNode: suggestions",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("prepare", prepare)
  .addNode("writer", writer)
  .addNode("suggestions", suggestions)
  .addEdge(START, "prepare")
  .addEdge("prepare", "writer")
  .addEdge("writer", "suggestions")
  .addEdge("suggestions", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
