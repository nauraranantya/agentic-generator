/**
 * Agent: feline-expert
 * ID: cat-one
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Returns a cat fact string from an external API (catfact.ninja).
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolGetCatFacts } from '../tools'

// Import memory
import { pgMemoryInstance } from '../memory'

/**
 * feline-expert
 * 
 * Instructions:
 * You are feline-expert.
 */
export const catOne = new Agent({
  id: `cat-one`,
  name: `feline-expert`,
  instructions: `You are feline-expert.`,
  model: 'openai/gpt-4o',
  tools: {
    toolGetCatFacts,
  },
  memory: pgMemoryInstance,
})
