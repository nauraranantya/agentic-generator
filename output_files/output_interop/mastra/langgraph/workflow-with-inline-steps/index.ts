import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});




/**
 * Node: taskStepOne
 * Agent: mastra_default_agent
 */
async function taskStepOne(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a workflow-executor." +
        "\nNode: taskStepOne",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskStepTwo
 * Agent: mastra_default_agent
 */
async function taskStepTwo(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a workflow-executor." +
        "\nNode: taskStepTwo",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("taskStepOne", taskStepOne)
  .addNode("taskStepTwo", taskStepTwo)
  .addEdge(START, "taskStepOne")
  .addEdge("taskStepOne", "taskStepTwo")
  .addEdge("taskStepTwo", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: my_workflow
