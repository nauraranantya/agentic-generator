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

// Tool: stock_prices_tool
const stock_prices_tool = tool(
  async () => {
    return "Result of stock_prices_tool";
  },
  {
    name: "stock_prices_tool",
    description: "Fetches the last day's closing stock price for a given symbol. Source tool implementation uses an HTTP fetch to https://mastra-stock-data.vercel.app/api/stock-data?symbol={symbol} and returns { symbol, currentPrice } with currentPrice mapped from data.prices['4. close'].",
    schema: z.object({}),
  }
);



/**
 * Node: fetchStockPriceForSymbolAaplExample
 * Agent: stock_agent
 */
async function fetchStockPriceForSymbolAaplExample(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level instruction used as the LLM system prompt / persona." +
        "\nNode: fetchStockPriceForSymbolAaplExample",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("fetchStockPriceForSymbolAaplExample", fetchStockPriceForSymbolAaplExample)
  .addEdge(START, "fetchStockPriceForSymbolAaplExample")
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: fetch_stock_price_pattern
// Workflow: Fetch Stock Price Pattern
