import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { ChatOpenAI } from "@langchain/openai";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

async function startAgent(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "System-level instruction provided to the LLM on each invocation. Used with the conversation messages array state.messages." +
        "\\nNode: startAgent",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("startAgent", startAgent)
  .addEdge(START, "startAgent")
  .addEdge("startAgent", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
