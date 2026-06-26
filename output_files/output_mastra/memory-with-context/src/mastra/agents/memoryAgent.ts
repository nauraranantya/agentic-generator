/**
 * Agent: assistant
 * ID: memory-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import memory
import { memoryKb } from '../memory'

/**
 * assistant
 * 
 * Instructions:
 * This prompt is supplied as the 'instructions' argument when creating the Agent instance in source code.
 */
export const memoryAgent = new Agent({
  id: `memory-agent`,
  name: `assistant`,
  instructions: `This prompt is supplied as the 'instructions' argument when creating the Agent instance in source code.`,
  model: 'openai/gpt-4o-mini',
  memory: memoryKb,
})
