import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";


const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

async function stepExtraction(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant / trip-planner." +
        "\nNode: stepExtraction",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}
async function stepClassify(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant / trip-planner." +
        "\nNode: stepClassify",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}
async function stepCallTools(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant / trip-planner." +
        "\nNode: stepCallTools",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}


const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("stepExtraction", stepExtraction)
  .addNode("stepClassify", stepClassify)
  .addNode("stepCallTools", stepCallTools)
  .addEdge("stepExtraction", "stepCallTools")
  .addEdge("stepClassify", "stepExtraction")
  .addEdge("stepClassify", "stepCallTools")
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
