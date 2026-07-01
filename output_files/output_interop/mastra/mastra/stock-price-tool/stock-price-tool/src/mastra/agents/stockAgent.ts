/**
 * Agent: assistant
 * ID: Stock Agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Fetch last day's closing stock price for a given symbol
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { stockPricesTool } from '../tools'

/**
 * assistant
 * 
 * Instructions:
 * You are assistant.
 */
export const stockAgent = new Agent({
  id: `Stock Agent`,
  name: `assistant`,
  instructions: `You are assistant.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    stockPricesTool,
  },
})
