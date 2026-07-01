/**
 * Agent: assistant
 * ID: langgraph_anthropic_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Find nearby pizza shop and return contact details (address, phone).
 *   - : Place an order at the specified pizza shop and return order confirmation.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { findPizzaTool, placeOrderTool } from '../tools'

/**
 * assistant
 * 
 * Instructions:
 * You are assistant.
 */
export const langgraphAnthropicAgent = new Agent({
  id: `langgraph_anthropic_agent`,
  name: `assistant`,
  instructions: `You are assistant.`,
  model: 'anthropic/claude-3-5-sonnet-latest',
  tools: {
    findPizzaTool,
    placeOrderTool,
  },
})
