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

// Tool: local_cmd_executor_tool
const local_cmd_executor_tool = tool(
  async () => {
    return "Result of local_cmd_executor_tool";
  },
  {
    name: "local_cmd_executor_tool",
    description: "Local command-line code executor used to run code with timeout and working directory.",
    schema: z.object({}),
  }
);



/**
 * Node: stockAnalysisYtdStockGainPlot
 * Agent: code_writer_agent
 */
async function stockAnalysisYtdStockGainPlot(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "The source obtains code_writer_agent.system_message and prints it; exact content is not available in the provided artifact." +
        "\nNode: stockAnalysisYtdStockGainPlot",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: stockAnalysisYtdStockGainPlot
 * Agent: code_writer_agent
 */
async function stockAnalysisYtdStockGainPlot(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "The source obtains code_writer_agent.system_message and prints it; exact content is not available in the provided artifact." +
        "\nNode: stockAnalysisYtdStockGainPlot",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("stockAnalysisYtdStockGainPlot", stockAnalysisYtdStockGainPlot)
  .addNode("stockAnalysisYtdStockGainPlot", stockAnalysisYtdStockGainPlot)
  .addEdge(START, "stockAnalysisYtdStockGainPlot")
  .addEdge("stockAnalysisYtdStockGainPlot", "stockAnalysisYtdStockGainPlot")
  .addEdge("stockAnalysisYtdStockGainPlot", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: l5_coding_financial_analysis_pattern
// Workflow: L5 Coding and Financial Analysis Pattern
