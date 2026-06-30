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

// Tool: cat_fact_tool
const cat_fact_tool = tool(
  async () => {
    return "Result of cat_fact_tool";
  },
  {
    name: "cat_fact_tool",
    description: "A tool",
    schema: z.object({}),
  }
);



/**
 * Node: stepOneTask
 * Agent: cat_one
 */
async function stepOneTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent role and long-form instructions provided in Agent instantiation (instructions in source code)." +
        "\nNode: stepOneTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stepTwoTask
 * Agent: cat_one
 */
async function stepTwoTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent role and long-form instructions provided in Agent instantiation (instructions in source code)." +
        "\nNode: stepTwoTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stepThreeTask
 * Agent: cat_one
 */
async function stepThreeTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent role and long-form instructions provided in Agent instantiation (instructions in source code)." +
        "\nNode: stepThreeTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stepFourTask
 * Agent: cat_one
 */
async function stepFourTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent role and long-form instructions provided in Agent instantiation (instructions in source code)." +
        "\nNode: stepFourTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stepFiveTask
 * Agent: cat_one
 */
async function stepFiveTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent role and long-form instructions provided in Agent instantiation (instructions in source code)." +
        "\nNode: stepFiveTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stepOneTask
 * Agent: cat_one
 */
async function stepOneTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent role and long-form instructions provided in Agent instantiation (instructions in source code)." +
        "\nNode: stepOneTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stepSixTask
 * Agent: cat_one
 */
async function stepSixTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent role and long-form instructions provided in Agent instantiation (instructions in source code)." +
        "\nNode: stepSixTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stepTwoTask
 * Agent: cat_one
 */
async function stepTwoTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent role and long-form instructions provided in Agent instantiation (instructions in source code)." +
        "\nNode: stepTwoTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stepThreeTask
 * Agent: cat_one
 */
async function stepThreeTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent role and long-form instructions provided in Agent instantiation (instructions in source code)." +
        "\nNode: stepThreeTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stepOneTask
 * Agent: cat_one
 */
async function stepOneTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent role and long-form instructions provided in Agent instantiation (instructions in source code)." +
        "\nNode: stepOneTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stepTwoTask
 * Agent: cat_one
 */
async function stepTwoTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent role and long-form instructions provided in Agent instantiation (instructions in source code)." +
        "\nNode: stepTwoTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stepThreeTask
 * Agent: cat_one
 */
async function stepThreeTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent role and long-form instructions provided in Agent instantiation (instructions in source code)." +
        "\nNode: stepThreeTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stepFourTask
 * Agent: cat_one
 */
async function stepFourTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent role and long-form instructions provided in Agent instantiation (instructions in source code)." +
        "\nNode: stepFourTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stepFiveTask
 * Agent: cat_one
 */
async function stepFiveTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent role and long-form instructions provided in Agent instantiation (instructions in source code)." +
        "\nNode: stepFiveTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stepOneTask
 * Agent: cat_one
 */
async function stepOneTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent role and long-form instructions provided in Agent instantiation (instructions in source code)." +
        "\nNode: stepOneTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stepTwoTask
 * Agent: cat_one
 */
async function stepTwoTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent role and long-form instructions provided in Agent instantiation (instructions in source code)." +
        "\nNode: stepTwoTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stepThreeTask
 * Agent: cat_one
 */
async function stepThreeTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent role and long-form instructions provided in Agent instantiation (instructions in source code)." +
        "\nNode: stepThreeTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stepOneTask
 * Agent: cat_one
 */
async function stepOneTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent role and long-form instructions provided in Agent instantiation (instructions in source code)." +
        "\nNode: stepOneTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(MastraSystemAnnotation)
  .addNode("stepOneTask", stepOneTask)
  .addNode("stepTwoTask", stepTwoTask)
  .addNode("stepThreeTask", stepThreeTask)
  .addNode("stepFourTask", stepFourTask)
  .addNode("stepFiveTask", stepFiveTask)
  .addNode("stepOneTask", stepOneTask)
  .addNode("stepSixTask", stepSixTask)
  .addNode("stepTwoTask", stepTwoTask)
  .addNode("stepThreeTask", stepThreeTask)
  .addNode("stepOneTask", stepOneTask)
  .addNode("stepTwoTask", stepTwoTask)
  .addNode("stepThreeTask", stepThreeTask)
  .addNode("stepFourTask", stepFourTask)
  .addNode("stepFiveTask", stepFiveTask)
  .addNode("stepOneTask", stepOneTask)
  .addNode("stepTwoTask", stepTwoTask)
  .addNode("stepThreeTask", stepThreeTask)
  .addNode("stepOneTask", stepOneTask)
  .addEdge(START, "stepOneTask")
  .addEdge("stepOneTask", "stepTwoTask")
  .addEdge("stepTwoTask", "stepThreeTask")
  .addEdge("stepThreeTask", "stepFourTask")
  .addEdge("stepFourTask", "stepFiveTask")
  .addEdge("stepOneTask", "stepSixTask")
  .addEdge("stepOneTask", "stepTwoTask")
  .addEdge("stepTwoTask", "stepFourTask")
  .addEdge("stepThreeTask", "stepFiveTask")
  .addEdge("stepOneTask", "stepTwoTask")
  .addEdge("stepTwoTask", "stepThreeTask")
  .addEdge("stepThreeTask", "stepOneTask")
  .addEdge("stepOneTask", "stepTwoTask")
  .addEdge("stepFiveTask", END)
  .addEdge("stepSixTask", END)
  .addEdge("stepTwoTask", END)
  .addEdge("stepThreeTask", END)
  .addEdge("stepFourTask", END)
  .addEdge("stepFiveTask", END)
;

export const graph = workflow.compile();
graph.name = "MastraSystem";
// Workflow: sequential_workflow_pattern
// Workflow: sequential-workflow pattern
// Workflow: parallel_workflow_pattern
// Workflow: parallel-workflow pattern
// Workflow: branched_workflow_pattern
// Workflow: branched-workflow pattern
// Workflow: cyclical_workflow_pattern
// Workflow: cyclical-workflow pattern
