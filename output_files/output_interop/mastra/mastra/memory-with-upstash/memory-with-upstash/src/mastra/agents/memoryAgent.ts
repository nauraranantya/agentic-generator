/**
 * Agent: Memory
 * ID: memory-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - Help user cook with available ingredients: Collective objective assigned to the Mastra system's agents to assist users in cooking with available ingredients.
 * Capabilities:
 *   - Key-value storage capability: Capability representing storing/retrieving messages or data in a key-value store.
 *   - Vector DB capability: Capability representing vector embedding storage and semantic recall operations.
 *   - Language model access capability: Capability to invoke and stream responses from a language model.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { memoryStorageUpstashTool, memoryVectorPgTool } from '../tools'

// Import memory
import { sharedConversationMemory } from '../memory'

/**
 * Memory
 * 
 * Instructions:
 * Agent-level instructions for Memory Agent; used as persistent agent prompt.
 */
export const memoryAgent = new Agent({
  id: `memory-agent`,
  name: `Memory`,
  instructions: `Agent-level instructions for Memory Agent; used as persistent agent prompt.`,
  model: 'openai/gpt-4o',
  tools: {
    memoryStorageUpstashTool,
    memoryVectorPgTool,
  },
  memory: sharedConversationMemory,
})
