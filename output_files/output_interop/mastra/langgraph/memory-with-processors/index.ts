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

// Tool: read_file_tool
const read_file_tool = tool(
  async () => {
    return "Result of read_file_tool";
  },
  {
    name: "read_file_tool",
    description: "Read a large file to test token limits; attempts several file system locations and otherwise generates a large mock file, returning a truncated 20K-character string.",
    schema: z.object({}),
  }
);
// Tool: search_tool
const search_tool = tool(
  async () => {
    return "Result of search_tool";
  },
  {
    name: "search_tool",
    description: "Search the web for information. Input schema expects a 'query' string.",
    schema: z.object({}),
  }
);



/**
 * Node: taskTokenLimiterDemo
 * Agent: token_test_agent
 */
async function taskTokenLimiterDemo(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Used as agent instructions to guide agent behavior in the Token Limiter demonstration." +
        "\nNode: taskTokenLimiterDemo",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskForgetfulInterviewerDemo
 * Agent: token_test_agent
 */
async function taskForgetfulInterviewerDemo(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Used as agent instructions to guide agent behavior in the Token Limiter demonstration." +
        "\nNode: taskForgetfulInterviewerDemo",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskTechnicalSupportDemo
 * Agent: token_test_agent
 */
async function taskTechnicalSupportDemo(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Used as agent instructions to guide agent behavior in the Token Limiter demonstration." +
        "\nNode: taskTechnicalSupportDemo",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("taskTokenLimiterDemo", taskTokenLimiterDemo)
  .addNode("taskForgetfulInterviewerDemo", taskForgetfulInterviewerDemo)
  .addNode("taskTechnicalSupportDemo", taskTechnicalSupportDemo)
  .addEdge(START, "taskTokenLimiterDemo")
  .addEdge("taskTokenLimiterDemo", "taskForgetfulInterviewerDemo")
  .addEdge("taskForgetfulInterviewerDemo", "taskTechnicalSupportDemo")
  .addEdge("taskTechnicalSupportDemo", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
