/**
 * Agent: price_provider
 * ID: stock-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - Fetch stock price capability: Capability to retrieve a last-close stock price for a given ticker symbol.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { stockPricesTool } from '../tools'

/**
 * price_provider
 * 
 * Instructions:
 * Agent-level instruction used as the LLM system prompt / persona.
 */
export const stockAgent = new Agent({
  id: `stock-agent`,
  name: `price_provider`,
  instructions: `Agent-level instruction used as the LLM system prompt / persona.`,
  model: 'openai/gpt-4o',
  tools: {
    stockPricesTool,
  },
})
