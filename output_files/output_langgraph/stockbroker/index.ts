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

// Tool: tool_stock_price
const tool_stock_price = tool(
  async () => {
    return "Result of tool_stock_price";
  },
  {
    name: "tool_stock_price",
    description: "A tool to get the stock price of a company. Invoked with argument { ticker: string }. When called, the agent fetches one-day and thirty-day price collections from https://api.financialdatasets.ai/prices with specified query parameters (interval, interval_multiplier, start_date, end_date, limit). The thirty-day retrieval may follow next_page_url to aggregate pages.",
    schema: z.object({}),
  }
);
// Tool: tool_portfolio
const tool_portfolio = tool(
  async () => {
    return "Result of tool_portfolio";
  },
  {
    name: "tool_portfolio",
    description: "A tool to get the user's portfolio details. Only called when the user explicitly requests portfolio details. Invoked with argument { get_portfolio: true }.",
    schema: z.object({}),
  }
);
// Tool: tool_buy_stock
const tool_buy_stock = tool(
  async () => {
    return "Result of tool_buy_stock";
  },
  {
    name: "tool_buy_stock",
    description: "A tool to buy a stock. Invoked with arguments { ticker: string, quantity: number }. When called, the agent requests a price snapshot from https://api.financialdatasets.ai/prices/snapshot and includes the snapshot and quantity in the UI output.",
    schema: z.object({}),
  }
);



/**
 * Node: callTools
 * Agent: stockbroker_01
 */
async function callTools(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "System-level instruction provided to the LLM on each invocation. Used with the conversation messages array state.messages." +
        "\nNode: callTools",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("callTools", callTools)
  .addEdge(START, "callTools")
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
