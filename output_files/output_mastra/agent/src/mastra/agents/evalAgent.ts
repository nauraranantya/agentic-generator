/**
 * Agent: Eval Agent
 * ID: eval-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { weatherInfoTool } from '../tools/weatherInfoTool'

// Import memory
import { globalMemory } from '../memory/globalMemory'

/**
 * Eval Agent
 * 
 */
export const evalAgent = new Agent({
  id: `eval-agent`,
  name: `Eval Agent`,
  instructions: ``,
  model: 'openai/gpt-4o',
  tools: {
    weatherInfoTool,
  },
  memory: globalMemory,
})
