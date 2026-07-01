/**
 * Agent: stockbroker
 * ID: stockbroker_01
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - Get stock prices: Capability to query historical and recent market prices for a given ticker.
 *   - Get portfolio: Capability to retrieve the user's portfolio details.
 *   - Buy stock: Capability to initiate a purchase action for a given stock and quantity.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolStockPrice, toolPortfolio, toolBuyStock } from '../tools'

/**
 * stockbroker
 * 
 * Instructions:
 * System-level instruction provided to the LLM on each invocation. Used with the conversation messages array state.messages.
 */
export const stockbroker01 = new Agent({
  id: `stockbroker_01`,
  name: `stockbroker`,
  instructions: `System-level instruction provided to the LLM on each invocation. Used with the conversation messages array state.messages.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolStockPrice,
    toolPortfolio,
    toolBuyStock,
  },
})
