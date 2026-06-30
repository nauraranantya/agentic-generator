/**
 * Agent: feline expert
 * ID: cat-one
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - fetch cat fact: Capability of the tool: retrieve a cat fact string from a remote API.
 *   - double numeric value: 
 *   - increment numeric value by 1: 
 *   - square numeric value: 
 *   - square root numeric value: 
 *   - triple numeric value: 
 *   - log numeric value and return raw text: 
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { catFactTool } from '../tools'

// Import memory
import { catOneMemory } from '../memory'

/**
 * feline expert
 * 
 * Instructions:
 * Agent role and long-form instructions provided in Agent instantiation (instructions in source code).
 */
export const catOne = new Agent({
  id: `cat-one`,
  name: `feline expert`,
  instructions: `Agent role and long-form instructions provided in Agent instantiation (instructions in source code).`,
  model: 'openai/gpt-4o',
  tools: {
    catFactTool,
  },
  memory: catOneMemory,
})
