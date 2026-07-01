/**
 * Agent: general_input_handler
 * ID: generalInput
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
import { toolStockbroker, toolTripPlanner, toolOpenCode, toolOrderPizza, toolWriterAgent } from '../tools'

/**
 * general_input_handler
 * 
 * Instructions:
 * You are general_input_handler.
 */
export const generalInput = new Agent({
  id: `generalInput`,
  name: `general_input_handler`,
  instructions: `You are general_input_handler.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolStockbroker,
    toolTripPlanner,
    toolOpenCode,
    toolOrderPizza,
    toolWriterAgent,
  },
})
