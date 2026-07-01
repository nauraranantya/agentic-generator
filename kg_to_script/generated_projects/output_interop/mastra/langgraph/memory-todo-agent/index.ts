import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});



// Define Agent: todo_agent
const todo_agent = async (state: typeof UnnamedProjectAnnotation.State) => {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    { role: "system", content: "You are a todolist manager." },
    ...state.messages,
  ]);
  return { messages: [response] };
};

const graph = new StateGraph(UnnamedProjectAnnotation)
  .addNode("initReturnChatTask", todo_agent)
  .addEdge(START, "initReturnChatTask")
  .addEdge("initReturnChatTask", END);

export const agent = graph.compile();
agent.name = "UnnamedProject";
// Workflow: todo_chat_loop
