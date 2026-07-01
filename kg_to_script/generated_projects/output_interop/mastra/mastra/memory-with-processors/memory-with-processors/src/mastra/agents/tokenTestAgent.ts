/**
 * Agent: LLM Agent
 * ID: token-test-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { readFileTool } from '../tools'

// Import memory
import { tokenTestMemory } from '../memory'

/**
 * LLM Agent
 * 
 * Instructions:
 * Used as agent instructions to guide agent behavior in the Token Limiter demonstration.
 */
export const tokenTestAgent = new Agent({
  id: `token-test-agent`,
  name: `LLM Agent`,
  instructions: `Used as agent instructions to guide agent behavior in the Token Limiter demonstration.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    readFileTool,
  },
  memory: tokenTestMemory,
})
