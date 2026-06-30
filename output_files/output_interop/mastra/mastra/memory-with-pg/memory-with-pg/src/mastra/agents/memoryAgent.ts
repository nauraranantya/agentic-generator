/**
 * Agent: Memory
 * ID: memory-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - use memory: Capability to store and recall conversation history via the SharedMemoryStore.
 *   - suggest recipes: Capability to propose recipes and high-level cooking steps given ingredient lists.
 */

import { Agent } from '@mastra/core/agent'

// Import memory
import { sharedMemoryStore } from '../memory'

/**
 * Memory
 * 
 * Instructions:
 * Agent-level instructions used as the system persona for the Memory Agent.
 */
export const memoryAgent = new Agent({
  id: `memory-agent`,
  name: `Memory`,
  instructions: `Agent-level instructions used as the system persona for the Memory Agent.`,
  model: 'openai/gpt-4o',
  memory: sharedMemoryStore,
})
