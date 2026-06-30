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

// Tool: file_read_tool
const file_read_tool = tool(
  async () => {
    return "Result of file_read_tool";
  },
  {
    name: "file_read_tool",
    description: "Tool used to read file contents (used by cv_reader and matcher).",
    schema: z.object({}),
  }
);
// Tool: csv_search_tool
const csv_search_tool = tool(
  async () => {
    return "Result of csv_search_tool";
  },
  {
    name: "csv_search_tool",
    description: "Tool used to search and parse CSV job listings (used by matcher).",
    schema: z.object({}),
  }
);
// Tool: my_custom_tool
const my_custom_tool = tool(
  async () => {
    return "Result of my_custom_tool";
  },
  {
    name: "my_custom_tool",
    description: "Custom tool implemented at src/match_to_proposal/tools/job_db_connect.py. Placeholder for an external DB connector. Implementation-specific behavior not modeled.",
    schema: z.object({}),
  }
);



/**
 * Node: readCvTask
 * Agent: cv_reader
 */
async function readCvTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level prompt to orient behavior. Use FileReadTool to access CV file. Produce a structured CV summary." +
        "\nNode: readCvTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: matchCvTask
 * Agent: matcher
 */
async function matchCvTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level prompt to orient behavior. Use CSVSearchTool and FileReadTool to access jobs CSV and CV summary." +
        "\nNode: matchCvTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("readCvTask", readCvTask)
  .addNode("matchCvTask", matchCvTask)
  .addEdge(START, "readCvTask")
  .addEdge("readCvTask", "matchCvTask")
  .addEdge("matchCvTask", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: match_to_proposal_workflow_pattern
// Workflow: next_pattern_placeholder
