/**
 * Agent: chef
 * ID: chef-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - Recipe suggestion: Capability: suggest recipes and high-level steps given available ingredients; described by the Chef Agent instructions.
 *   - Memory recall and conversation continuity: Capability: recall past messages and maintain long-running conversation states.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { openaiTool, mongoDbStore } from '../tools'

// Import memory
import { mastraMemory } from '../memory'

/**
 * chef
 * 
 * Instructions:
 * You are chef.
 */
export const chefAgent = new Agent({
  id: `chef-agent`,
  name: `chef`,
  instructions: `You are chef.`,
  model: 'openai/gpt-4o',
  tools: {
    openaiTool,
    mongoDbStore,
  },
  memory: mastraMemory,
})
