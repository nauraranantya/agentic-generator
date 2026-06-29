import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";


const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

const graph = new StateGraph(UnnamedProjectAnnotation)
  .addNode("chat", async (state) => {
    const model = new ChatOpenAI({ model: "gpt-4o-mini" });
    const response = await model.invoke([
      { role: "system", content: "This system role message is prepended to every model invocation in the chat node." },
      ...state.messages,
    ]);
    return { messages: [response] };
  })
  .addEdge(START, "chat")
  .addEdge("chat", END);

export const agent = graph.compile();
agent.name = "UnnamedProject";
