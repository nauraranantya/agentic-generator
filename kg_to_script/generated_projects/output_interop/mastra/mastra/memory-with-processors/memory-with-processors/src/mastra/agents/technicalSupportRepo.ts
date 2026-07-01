/**
 * Agent: LLM Agent
 * ID: technical-support-repo
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { searchTool } from '../tools'

// Import memory
import { supportAgentMemoryRepo } from '../memory'

/**
 * LLM Agent
 * 
 * Instructions:
 * You are LLM Agent.
 */
export const technicalSupportRepo = new Agent({
  id: `technical-support-repo`,
  name: `LLM Agent`,
  instructions: `You are LLM Agent.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    searchTool,
  },
  memory: supportAgentMemoryRepo,
})
