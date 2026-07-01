import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";

const MastraSystemAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});



// Define Agent: chef_agent
const chef_agent = async (state: typeof MastraSystemAnnotation.State) => {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    { role: "system", content: "This prompt is set as the chefAgent's instruction/role definition (provided as 'instructions' when the agent is created)." },
    ...state.messages,
  ]);
  return { messages: [response] };
};
// Define Agent: memory_agent
const memory_agent = async (state: typeof MastraSystemAnnotation.State) => {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    { role: "system", content: "This prompt is set as the memoryAgent's instruction/role definition (provided as 'instructions' when the agent is created)." },
    ...state.messages,
  ]);
  return { messages: [response] };
};

const graph = new StateGraph(MastraSystemAnnotation)
  .addNode("taskInitialIngredientsQuery", chef_agent)
  .addEdge(START, "taskInitialIngredientsQuery")
  .addEdge("taskInitialIngredientsQuery", END);

export const agent = graph.compile();
agent.name = "MastraSystem";
// Workflow: chef_conversation_pattern
// Workflow: Chef Conversation Pattern
