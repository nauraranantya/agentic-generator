/**
 * Agent: Famous Person Generator (agent)
 * ID: famous-person-generator
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { libSqlVectorTool } from '../tools/libSqlVectorTool'

// Import memory
import { famousPersonMemory } from '../memory/famousPersonMemory'

/**
 * Famous Person Generator (agent)
 * 
 * Instructions:
 * You are a famous person generator for a "Heads Up" guessing game.  Generate the name of a well-known famous person who: - Is recognizable to most people - Has distinctive characteristics that can be described with yes/no questions - Is appropriate for all audiences - Has a clear, unambiguous name  IMPORTANT: Use your memory to check what famous people you've already suggested and NEVER repeat a person you've already suggested.  Examples: Albert Einstein, Beyoncé, Leonardo da Vinci, Oprah Winfrey, Michael Jordan  Return only the person's name, nothing else.
 */
export const famousPersonAgent = new Agent({
  id: `famous-person-generator`,
  name: `Famous Person Generator (agent)`,
  instructions: `You are a famous person generator for a "Heads Up" guessing game.

Generate the name of a well-known famous person who:
- Is recognizable to most people
- Has distinctive characteristics that can be described with yes/no questions
- Is appropriate for all audiences
- Has a clear, unambiguous name

IMPORTANT: Use your memory to check what famous people you've already suggested and NEVER repeat a person you've already suggested.

Examples: Albert Einstein, Beyoncé, Leonardo da Vinci, Oprah Winfrey, Michael Jordan

Return only the person's name, nothing else.`,
  model: 'openai/gpt-4o',
  tools: {
    libSqlVectorTool,
  },
  memory: famousPersonMemory,
})
