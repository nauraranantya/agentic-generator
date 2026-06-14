/**
 * Agent: Chef Network
 * ID: network-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { cookingTool } from '../tools/cookingTool'
import { weatherInfoTool } from '../tools/weatherInfoTool'

// Import memory
import { globalMemory } from '../memory/globalMemory'

/**
 * Chef Network
 * 
 */
export const networkAgent = new Agent({
  id: `network-agent`,
  name: `Chef Network`,
  instructions: ``,
  model: 'openai/gpt-4o-mini',
  tools: {
    cookingTool,
    weatherInfoTool,
  },
  memory: globalMemory,
})
