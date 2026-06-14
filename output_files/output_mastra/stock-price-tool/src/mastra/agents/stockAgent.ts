/**
 * Agent: Stock Agent
 * ID: stock-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { stockPricesTool } from '../tools/stockPricesTool'

/**
 * Stock Agent
 * 
 * Instructions:
 * You are a helpful assistant that provides current stock prices. When asked about a stock, use the stock price tool to fetch the stock price.
 */
export const stockAgent = new Agent({
  id: `stock-agent`,
  name: `Stock Agent`,
  instructions: `You are a helpful assistant that provides current stock prices. When asked about a stock, use the stock price tool to fetch the stock price.`,
  model: 'openai/gpt-4o',
  tools: {
    stockPricesTool,
  },
})
