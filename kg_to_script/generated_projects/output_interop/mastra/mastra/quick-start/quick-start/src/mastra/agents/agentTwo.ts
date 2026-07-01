/**
 * Agent: assistant
 * ID: Agent Two
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Execute workflow step code and perform system actions (e.g., logging).
 */

import { Agent } from '@mastra/core/agent'

/**
 * assistant
 * 
 * Instructions:
 * No explicit goal provided in source; placeholder goal.
 */
export const agentTwo = new Agent({
  id: `Agent Two`,
  name: `assistant`,
  instructions: `No explicit goal provided in source; placeholder goal.`,
  model: 'openai/gpt-4o-mini',
})
