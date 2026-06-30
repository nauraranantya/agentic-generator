import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: mastra_engine_tool
const mastra_engine_tool = tool(
  async () => {
    return "Result of mastra_engine_tool";
  },
  {
    name: "mastra_engine_tool",
    description: "Represents the Mastra runtime/engine that executes workflow steps and tasks (mapped to :Tool for lack of a runtime class in ontology).",
    schema: z.object({}),
  }
);



/**
 * Node: taskStepOne
 * Agent: defaultAgent
 */
async function taskStepOne(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a helpful assistant." +
        "\\nNode: taskStepOne",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskStepTwo
 * Agent: defaultAgent
 */
async function taskStepTwo(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a helpful assistant." +
        "\\nNode: taskStepTwo",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskStepThree
 * Agent: defaultAgent
 */
async function taskStepThree(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a helpful assistant." +
        "\\nNode: taskStepThree",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("taskStepOne", taskStepOne)
  .addNode("taskStepTwo", taskStepTwo)
  .addNode("taskStepThree", taskStepThree)
  .addEdge(START, "taskStepOne")
  .addEdge("taskStepOne", "taskStepTwo")
  .addEdge("taskStepTwo", "taskStepThree")
  .addEdge("taskStepThree", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: my_workflow_pattern
