/**
 * Agent: stockbroker_tool_agent
 * ID: stockbroker
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Fetch price, buy/sell tickers, retrieve user portfolio.
 *   - : Suggest restaurants, hotels, and itineraries for locations.
 *   - : Generate project code (React TODO app) and related files.
 *   - : Place pizza orders and return confirmation details.
 *   - : Generate long-form text documents or writing deliverables.
 *   - : Select the appropriate target route/tool based on user input.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolStockbroker } from '../tools'

/**
 * stockbroker_tool_agent
 * 
 * Instructions:
 * You are stockbroker_tool_agent.
 */
export const stockbroker = new Agent({
  id: `stockbroker`,
  name: `stockbroker_tool_agent`,
  instructions: `You are stockbroker_tool_agent.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolStockbroker,
  },
})
