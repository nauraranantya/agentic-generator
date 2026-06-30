import { ChatAnthropic } from "@langchain/anthropic";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: yc_directory_tool
const yc_directory_tool = tool(
  async () => {
    return "Result of yc_directory_tool";
  },
  {
    name: "yc_directory_tool",
    description: "Tool that returns the Y Combinator 2024 directory data. Created in src/mastra/tools/index.ts. Exposes an execute action that returns the dataset.",
    schema: z.object({}),
  }
);
// Tool: mastra_evals_runner
const mastra_evals_runner = tool(
  async () => {
    return "Result of mastra_evals_runner";
  },
  {
    name: "mastra_evals_runner",
    description: "Represents the runEvals invocation in src/mastra/tests/index.ts. Executes an evaluation run on a target agent using a set of scorer capabilities and data inputs.",
    schema: z.object({}),
  }
);



/**
 * Node: runEvalsTask
 * Agent: yc_directory_agent
 */
async function runEvalsTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Used as agent-level instructions for ycDirectoryAgent (src/mastra/agents/index.ts)." +
        "\\nNode: runEvalsTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: fetchYcDataTask
 * Agent: yc_directory_agent
 */
async function fetchYcDataTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Used as agent-level instructions for ycDirectoryAgent (src/mastra/agents/index.ts)." +
        "\\nNode: fetchYcDataTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: answerYcDirectoryQuery
 * Agent: yc_directory_agent
 */
async function answerYcDirectoryQuery(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Used as agent-level instructions for ycDirectoryAgent (src/mastra/agents/index.ts)." +
        "\\nNode: answerYcDirectoryQuery",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("runEvalsTask", runEvalsTask)
  .addNode("fetchYcDataTask", fetchYcDataTask)
  .addNode("answerYcDirectoryQuery", answerYcDirectoryQuery)
  .addEdge(START, "runEvalsTask")
  .addEdge("runEvalsTask", "fetchYcDataTask")
  .addEdge("fetchYcDataTask", "answerYcDirectoryQuery")
  .addEdge("answerYcDirectoryQuery", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: yc_query_workflow
