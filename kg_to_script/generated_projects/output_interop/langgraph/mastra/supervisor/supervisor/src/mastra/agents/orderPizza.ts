/**
 * Agent: order_pizza_tool_agent
 * ID: orderPizza
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
import { toolOrderPizza } from '../tools'

/**
 * order_pizza_tool_agent
 * 
 * Instructions:
 * You are order_pizza_tool_agent.
 */
export const orderPizza = new Agent({
  id: `orderPizza`,
  name: `order_pizza_tool_agent`,
  instructions: `You are order_pizza_tool_agent.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolOrderPizza,
  },
})
