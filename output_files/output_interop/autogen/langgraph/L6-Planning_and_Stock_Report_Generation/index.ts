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

// Tool: coding_environment_tool
const coding_environment_tool = tool(
  async () => {
    return "Result of coding_environment_tool";
  },
  {
    name: "coding_environment_tool",
    description: "Conceptual tool representing the environment used by Executor to run code. Config captured as key/value on Config individual.",
    schema: z.object({}),
  }
);



/**
 * Node: mainTask
 * Agent: planner_agent
 */
async function mainTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Planner. Given a task, determine what information is needed to complete the task. After each step is done by others, check the progress and instruct the remaining steps" +
        "\\nNode: mainTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: planInformationTask
 * Agent: planner_agent
 */
async function planInformationTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Planner. Given a task, determine what information is needed to complete the task. After each step is done by others, check the progress and instruct the remaining steps" +
        "\\nNode: planInformationTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: writeCodeTask
 * Agent: engineer_agent
 */
async function writeCodeTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Engineer: writes code per planner's plan" +
        "\\nNode: writeCodeTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: executeCodeTask
 * Agent: executor_agent
 */
async function executeCodeTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Executor: execute code and return execution results (no human input)." +
        "\\nNode: executeCodeTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: writeReportTask
 * Agent: writer_agent
 */
async function writeReportTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Writer: write blogs based on the code execution results and take feedback from the admin to refine the blog." +
        "\\nNode: writeReportTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: adminFeedbackTask
 * Agent: planner_agent
 */
async function adminFeedbackTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Planner. Given a task, determine what information is needed to complete the task. After each step is done by others, check the progress and instruct the remaining steps" +
        "\\nNode: adminFeedbackTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("mainTask", mainTask)
  .addNode("planInformationTask", planInformationTask)
  .addNode("writeCodeTask", writeCodeTask)
  .addNode("executeCodeTask", executeCodeTask)
  .addNode("writeReportTask", writeReportTask)
  .addNode("adminFeedbackTask", adminFeedbackTask)
  .addEdge(START, "mainTask")
  .addEdge("mainTask", "planInformationTask")
  .addEdge("planInformationTask", "writeCodeTask")
  .addEdge("writeCodeTask", "executeCodeTask")
  .addEdge("executeCodeTask", "writeReportTask")
  .addEdge("writeReportTask", "adminFeedbackTask")
  .addEdge("adminFeedbackTask", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: stock_report_generation_pattern
