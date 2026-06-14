/**
 * Agent: Chef Agent Responses
 * ID: chef-agent-responses
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
 * Chef Agent Responses
 * 
 */
export const chefAgentResponses = new Agent({
  id: `chef-agent-responses`,
  name: `Chef Agent Responses`,
  instructions: ``,
  model: 'openai/gpt-4o',
  tools: {
    cookingTool,
    weatherInfoTool,
  },
  memory: chefAgentMemory,
})
