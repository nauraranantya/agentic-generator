/**
 * Agent: generator
 * ID: famous-person-generator
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - Heads-Up game objective: Objective: run an interactive Heads-Up guessing game to let the user identify a famous person via yes/no questions and guesses.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { libSqlVectorTool } from '../tools'

// Import memory
import { famousPersonMemory } from '../memory'

/**
 * generator
 * 
 * Instructions:
 * Agent instructions and constraints for generating a single famous person's name.
 */
export const famousPersonGenerator = new Agent({
  id: `famous-person-generator`,
  name: `generator`,
  instructions: `Agent instructions and constraints for generating a single famous person's name.`,
  model: 'openai/gpt-4o',
  tools: {
    libSqlVectorTool,
  },
  memory: famousPersonMemory,
})
