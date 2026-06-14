/**
 * Agent: Stock + Weather Agent
 * ID: stock-weather-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { stockPriceTool } from '../tools/stockPriceTool'
import { weatherTool } from '../tools/weatherTool'

/**
 * Stock + Weather Agent
 * 
 * Instructions:
 * You are a helpful assistant that provides current stock prices. When asked about a stock, use the stock price tool to fetch the stock price. You also love to check the weather when your stock market buddies ask you what the weather is.
 */
export const stockWeatherAgent = new Agent({
  id: `stock-weather-agent`,
  name: `Stock + Weather Agent`,
  instructions: `You are a helpful assistant that provides current stock prices. When asked about a stock, use the stock price tool to fetch the stock price. You also love to check the weather when your stock market buddies ask you what the weather is.`,
  model: 'openai/gpt-4o',
  tools: {
    stockPriceTool,
    weatherTool,
  },
})
