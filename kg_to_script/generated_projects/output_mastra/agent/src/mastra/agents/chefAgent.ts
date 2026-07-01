/**
 * Agent: Chef
 * ID: Chef Agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Executes the tool's registered logic (no input schema required)
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { myTool } from '../tools'

/**
 * Chef
 * 
 * Instructions:
 * You are Chef.
 */
export const chefAgent = new Agent({
  id: `Chef Agent`,
  name: `Chef`,
  instructions: `You are Chef.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    myTool,
  },
})
