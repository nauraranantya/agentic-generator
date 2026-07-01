import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});



// Define Agent: chef_agent
const chef_agent = async (state: typeof UnnamedProjectAnnotation.State) => {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    { role: "system", content: "Agent-level instructions used as the system persona for the Chef Agent." },
    ...state.messages,
  ]);
  return { messages: [response] };
};
// Define Agent: memory_agent
const memory_agent = async (state: typeof UnnamedProjectAnnotation.State) => {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    { role: "system", content: "Agent-level instructions used as the system persona for the Memory Agent." },
    ...state.messages,
  ]);
  return { messages: [response] };
};

const graph = new StateGraph(UnnamedProjectAnnotation)
  .addNode("taskRecipeSuggestInitialQuery", chef_agent)
  .addEdge(START, "taskRecipeSuggestInitialQuery")
  .addEdge("taskRecipeSuggestInitialQuery", END);

export const agent = graph.compile();
agent.name = "UnnamedProject";
// Workflow: recipe_workflow_pattern
// Workflow: conversation_with_memory_pattern
