import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";

const MastraSystemAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});



// Define Agent: weather_agent
const weather_agent = async (state: typeof MastraSystemAnnotation.State) => {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    { role: "system", content: "You are a weather assistant." },
    ...state.messages,
  ]);
  return { messages: [response] };
};

const graph = new StateGraph(MastraSystemAnnotation)
  .addNode("networkSupervisorTask", weather_agent)
  .addEdge(START, "networkSupervisorTask")
  .addEdge("networkSupervisorTask", END);

export const agent = graph.compile();
agent.name = "MastraSystem";
// Workflow: my_network_pattern
// Workflow: myNetwork
