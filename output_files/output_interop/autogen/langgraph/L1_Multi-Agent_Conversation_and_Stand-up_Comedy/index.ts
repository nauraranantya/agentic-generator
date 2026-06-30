import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});



// Define Agent: cathy
const cathy = async (state: typeof UnnamedProjectAnnotation.State) => {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    { role: "system", content: "System message as provided at ConversableAgent creation in the notebook." },
    ...state.messages,
  ]);
  return { messages: [response] };
};
// Define Agent: joe
const joe = async (state: typeof UnnamedProjectAnnotation.State) => {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    { role: "system", content: "System message as provided at ConversableAgent creation in the notebook." },
    ...state.messages,
  ]);
  return { messages: [response] };
};

const graph = new StateGraph(UnnamedProjectAnnotation)
  .addNode("chat", cathy)
  .addEdge(START, "chat")
  .addEdge("chat", END);

export const agent = graph.compile();
agent.name = "UnnamedProject";
