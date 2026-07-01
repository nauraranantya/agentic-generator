/**
 * Agent: trading_assistant
 * ID: trade_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Execute market buy orders for a specified ticker and quantity at the provided price.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { buyStockTool } from '../tools'

/**
 * trading_assistant
 * 
 * Instructions:
 * You are trading_assistant.
 */
export const tradeAgent = new Agent({
  id: `trade_agent`,
  name: `trading_assistant`,
  instructions: `You are trading_assistant.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    buyStockTool,
  },
})
