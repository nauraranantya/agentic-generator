/**
 * Agent: Memory Agent
 * ID: memory-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import memory
import { memoryKb } from '../memory/memoryKb'

/**
 * Memory Agent
 * 
 * Instructions:
 * You are a helpful AI agent, looking to assist however you can.
 */
export const memoryAgent = new Agent({
  id: `memory-agent`,
  name: `Memory Agent`,
  instructions: `You are a helpful AI agent, looking to assist however you can.`,
  model: 'openai/gpt-4o-mini',
  memory: memoryKb,
})
