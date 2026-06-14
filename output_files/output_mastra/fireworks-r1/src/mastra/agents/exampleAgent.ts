/**
 * Agent: Example Agent
 * ID: example-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import memory
import { exampleAgentMemory } from '../memory/exampleAgentMemory'

/**
 * Example Agent
 * 
 * Instructions:
 * You are a helpful and intelligent AI agent.
 */
export const exampleAgent = new Agent({
  id: `example-agent`,
  name: `Example Agent`,
  instructions: `You are a helpful and intelligent AI agent.`,
  model: 'accounts/fireworks/models/deepseek-r1',
  memory: exampleAgentMemory,
})
