/**
 * Agent: Chef Agent
 * ID: chef-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { cookingTool } from '../tools/cookingTool'
import { weatherInfoTool } from '../tools/weatherInfoTool'

// Import memory
import { chefAgentMemory } from '../memory/chefAgentMemory'

/**
 * Chef Agent
 * 
 */
export const chefAgent = new Agent({
  id: `chef-agent`,
  name: `Chef Agent`,
  instructions: ``,
  model: 'openai/gpt-4o-mini',
  tools: {
    cookingTool,
    weatherInfoTool,
  },
  memory: chefAgentMemory,
})
