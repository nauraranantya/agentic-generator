/**
 * Agent: LLM Agent
 * ID: stock-weather-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : Objective grouping the sub-tasks needed to respond to the user (get weather, get stock price, compose reply).
 * Capabilities:
 *   - : Capability to fetch the most recent closing stock price for a provided stock symbol (getStockPrice).
 *   - : Capability to get current weather for a specified location (getWeather). Performs geocoding, then queries a weather API, and returns a structured JSON response.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { stockPriceTool, weatherTool } from '../tools'

/**
 * LLM Agent
 * 
 * Instructions:
 * Agent-level system instructions for independent operation (agent behavior and role).
 */
export const stockWeatherAgent = new Agent({
  id: `stock-weather-agent`,
  name: `LLM Agent`,
  instructions: `Agent-level system instructions for independent operation (agent behavior and role).`,
  model: 'openai/gpt-4o',
  tools: {
    stockPriceTool,
    weatherTool,
  },
})
