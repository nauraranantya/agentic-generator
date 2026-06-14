/**
 * Agent: Dynamic Agent
 * ID: dynamic-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { cookingTool } from '../tools/cookingTool'

// Import memory
import { globalMemory } from '../memory/globalMemory'

/**
 * Dynamic Agent
 * 
 */
export const dynamicAgent = new Agent({
  id: `dynamic-agent`,
  name: `Dynamic Agent`,
  instructions: ``,
  model: 'openai/gpt-4o',
  tools: {
    cookingTool,
  },
  memory: globalMemory,
})
