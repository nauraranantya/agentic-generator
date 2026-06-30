import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});



// Define Agent: meta_quest_expert
const meta_quest_expert = async (state: typeof UnnamedProjectAnnotation.State) => {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    { role: "system", content: "Agent-level instruction/backstory used to guide the agent's independent reasoning and responses." },
    ...state.messages,
  ]);
  return { messages: [response] };
};

const graph = new StateGraph(UnnamedProjectAnnotation)
  .addNode("answerQuestionTask", meta_quest_expert)
  .addEdge(START, "answerQuestionTask")
  .addEdge("answerQuestionTask", END);

export const agent = graph.compile();
agent.name = "UnnamedProject";
// Workflow: meta_quest_sequential_workflow
