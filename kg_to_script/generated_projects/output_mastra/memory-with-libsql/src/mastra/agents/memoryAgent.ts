/**
 * Agent: memory
 * ID: memory-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import memory
import { mastraMemory } from '../memory'

/**
 * memory
 * 
 * Instructions:
 * This prompt is set as the memoryAgent's instruction/role definition (provided as 'instructions' when the agent is created).
 */
export const memoryAgent = new Agent({
  id: `memory-agent`,
  name: `memory`,
  instructions: `This prompt is set as the memoryAgent's instruction/role definition (provided as 'instructions' when the agent is created).`,
  model: 'openai/gpt-4o-mini',
  memory: mastraMemory,
})
