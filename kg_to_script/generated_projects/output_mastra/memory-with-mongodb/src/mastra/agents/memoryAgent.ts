/**
 * Agent: memory
 * ID: memory-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - Recipe suggestion: Capability: suggest recipes and high-level steps given available ingredients; described by the Chef Agent instructions.
 *   - Memory recall and conversation continuity: Capability: recall past messages and maintain long-running conversation states.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { openaiTool, mongoDbStore, mongoDbVector } from '../tools'

// Import memory
import { mastraMemory } from '../memory'

/**
 * memory
 * 
 * Instructions:
 * You are memory.
 */
export const memoryAgent = new Agent({
  id: `memory-agent`,
  name: `memory`,
  instructions: `You are memory.`,
  model: 'openai/gpt-4o',
  tools: {
    openaiTool,
    mongoDbStore,
    mongoDbVector,
  },
  memory: mastraMemory,
})
