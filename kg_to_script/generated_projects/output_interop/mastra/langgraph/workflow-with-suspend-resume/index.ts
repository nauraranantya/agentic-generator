import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const MastraSystemAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: mastra_runtime
const mastra_runtime = tool(
  async () => {
    return "Result of mastra_runtime";
  },
  {
    name: "mastra_runtime",
    description: "Logical runtime tool that executes workflow steps and coordinates suspend/resume behavior.",
    schema: z.object({}),
  }
);
// Tool: libsql_store
const libsql_store = tool(
  async () => {
    return "Result of libsql_store";
  },
  {
    name: "libsql_store",
    description: "Storage plugin used by Mastra for workflow snapshots.",
    schema: z.object({}),
  }
);



/**
 * Node: invokeNestedDataProcessingWorkflow
 * Agent: defaultAgent
 */
async function invokeNestedDataProcessingWorkflow(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a helpful assistant." +
        "\\nNode: invokeNestedDataProcessingWorkflow",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stepOneTaskDoubleInput
 * Agent: defaultAgent
 */
async function stepOneTaskDoubleInput(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a helpful assistant." +
        "\\nNode: stepOneTaskDoubleInput",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: resumeIncrement
 * Agent: defaultAgent
 */
async function resumeIncrement(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a helpful assistant." +
        "\\nNode: resumeIncrement",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stepThreeTaskTripleIncrementedValue
 * Agent: defaultAgent
 */
async function stepThreeTaskTripleIncrementedValue(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a helpful assistant." +
        "\\nNode: stepThreeTaskTripleIncrementedValue",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stepFourTaskIsEvenCheck
 * Agent: defaultAgent
 */
async function stepFourTaskIsEvenCheck(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a helpful assistant." +
        "\\nNode: stepFourTaskIsEvenCheck",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(MastraSystemAnnotation)
  .addNode("invokeNestedDataProcessingWorkflow", invokeNestedDataProcessingWorkflow)
  .addNode("stepOneTaskDoubleInput", stepOneTaskDoubleInput)
  .addNode("resumeIncrement", resumeIncrement)
  .addNode("stepThreeTaskTripleIncrementedValue", stepThreeTaskTripleIncrementedValue)
  .addNode("stepFourTaskIsEvenCheck", stepFourTaskIsEvenCheck)
  .addEdge(START, "invokeNestedDataProcessingWorkflow")
  .addEdge("invokeNestedDataProcessingWorkflow", "stepOneTaskDoubleInput")
  .addEdge("stepOneTaskDoubleInput", "resumeIncrement")
  .addEdge("resumeIncrement", "stepThreeTaskTripleIncrementedValue")
  .addEdge("stepThreeTaskTripleIncrementedValue", "stepFourTaskIsEvenCheck")
  .addEdge("stepFourTaskIsEvenCheck", END)
;

export const graph = workflow.compile();
graph.name = "MastraSystem";
// Workflow: my_workflow
// Workflow: my-workflow
// Workflow: data_processing
// Workflow: data-processing
