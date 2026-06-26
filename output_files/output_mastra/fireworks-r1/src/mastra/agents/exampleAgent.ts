/**
 * Agent: assistant
 * ID: example-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import memory
import { exampleAgentMemory } from '../memory'

/**
 * assistant
 * 
 * Instructions:
 * System-level instruction (agent 'instructions' argument)
 */
export const exampleAgent = new Agent({
  id: `example-agent`,
  name: `assistant`,
  instructions: `System-level instruction (agent 'instructions' argument)`,
  model: 'openai/gpt-4o-mini',
  memory: exampleAgentMemory,
})
