import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const MastrasystemAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: search_crypto_coins_tool
const search_crypto_coins_tool = tool(
  async () => {
    return "Result of search_crypto_coins_tool";
  },
  {
    name: "search_crypto_coins_tool",
    description: "Tool to search all available crypto coins by a keyword. Implements logic: fetch coin list from CoinGecko, try exact match by name (case-insensitive), if not found return first coin whose name contains the keyword.",
    schema: z.object({}),
  }
);
// Tool: get_crypto_price_tool
const get_crypto_price_tool = tool(
  async () => {
    return "Result of get_crypto_price_tool";
  },
  {
    name: "get_crypto_price_tool",
    description: "Tool to get crypto price by coin id. Fetches market data for a given id from CoinGecko markets endpoint.",
    schema: z.object({}),
  }
);
// Tool: get_historical_crypto_prices_tool
const get_historical_crypto_prices_tool = tool(
  async () => {
    return "Result of get_historical_crypto_prices_tool";
  },
  {
    name: "get_historical_crypto_prices_tool",
    description: "Tool to retrieve historical price data for a coin. Returns an array of {timestamp,price}. Calls CoinGecko market_chart endpoint.",
    schema: z.object({}),
  }
);



/**
 * Node: searchCryptoCoinsTask
 * Agent: crypto_agent
 */
async function searchCryptoCoinsTask(state: typeof MastrasystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a crypto-agent." +
        "\nNode: searchCryptoCoinsTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: getCryptoPriceTask
 * Agent: crypto_agent
 */
async function getCryptoPriceTask(state: typeof MastrasystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a crypto-agent." +
        "\nNode: getCryptoPriceTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: getHistoricalCryptoPricesTask
 * Agent: crypto_agent
 */
async function getHistoricalCryptoPricesTask(state: typeof MastrasystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a crypto-agent." +
        "\nNode: getHistoricalCryptoPricesTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(MastrasystemAnnotation)
  .addNode("searchCryptoCoinsTask", searchCryptoCoinsTask)
  .addNode("getCryptoPriceTask", getCryptoPriceTask)
  .addNode("getHistoricalCryptoPricesTask", getHistoricalCryptoPricesTask)
  .addEdge(START, "searchCryptoCoinsTask")
  .addEdge("searchCryptoCoinsTask", "getCryptoPriceTask")
  .addEdge("getCryptoPriceTask", "getHistoricalCryptoPricesTask")
  .addEdge("getHistoricalCryptoPricesTask", END)
;

export const graph = workflow.compile();
graph.name = "Mastrasystem";
// Workflow: crypto_workflow_pattern
// Workflow: Crypto workflow pattern
