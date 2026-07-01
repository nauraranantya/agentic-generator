/**
 * Agent: chef
 * ID: chef-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import memory
import { mastraMemory } from '../memory'

/**
 * chef
 * 
 * Instructions:
 * This prompt is set as the chefAgent's instruction/role definition (provided as 'instructions' when the agent is created).
 */
export const chefAgent = new Agent({
  id: `chef-agent`,
  name: `chef`,
  instructions: `This prompt is set as the chefAgent's instruction/role definition (provided as 'instructions' when the agent is created).`,
  model: 'openai/gpt-4o-mini',
  memory: mastraMemory,
})
