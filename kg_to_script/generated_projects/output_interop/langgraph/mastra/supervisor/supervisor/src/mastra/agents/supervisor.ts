/**
 * Agent: supervisor
 * ID: supervisor
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
import { toolStockbroker, toolTripPlanner, toolOpenCode, toolOrderPizza, toolWriterAgent, toolRouter } from '../tools'

/**
 * supervisor
 * 
 * Instructions:
 * You are supervisor.
 */
export const supervisor = new Agent({
  id: `supervisor`,
  name: `supervisor`,
  instructions: `You are supervisor.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolStockbroker,
    toolTripPlanner,
    toolOpenCode,
    toolOrderPizza,
    toolWriterAgent,
    toolRouter,
  },
})
