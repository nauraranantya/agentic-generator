/**
 * Agent: Chef Agent V2 Model
 * ID: chef-model-v2-agent
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
 * Chef Agent V2 Model
 * 
 */
export const chefModelV2Agent = new Agent({
  id: `chef-model-v2-agent`,
  name: `Chef Agent V2 Model`,
  instructions: ``,
  model: 'openai/gpt-4o-mini',
  tools: {
    cookingTool,
    weatherInfoTool,
  },
  memory: chefAgentMemory,
})
