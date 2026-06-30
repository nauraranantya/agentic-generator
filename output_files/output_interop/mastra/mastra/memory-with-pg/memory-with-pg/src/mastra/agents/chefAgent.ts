/**
 * Agent: Chef
 * ID: chef-agent
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
 * Chef
 * 
 * Instructions:
 * Agent-level instructions used as the system persona for the Chef Agent.
 */
export const chefAgent = new Agent({
  id: `chef-agent`,
  name: `Chef`,
  instructions: `Agent-level instructions used as the system persona for the Chef Agent.`,
  model: 'openai/gpt-4o',
  memory: sharedMemoryStore,
})
