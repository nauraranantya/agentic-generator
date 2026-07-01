/**
 * Agent: LLM Agent
 * ID: technical-support
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { searchTool } from '../tools'

// Import memory
import { techSupportMemoryDemo } from '../memory'

/**
 * LLM Agent
 * 
 * Instructions:
 * Agent system instructions controlling behavior and style (support-agent.ts).
 */
export const technicalSupport = new Agent({
  id: `technical-support`,
  name: `LLM Agent`,
  instructions: `Agent system instructions controlling behavior and style (support-agent.ts).`,
  model: 'openai/gpt-4o-mini',
  tools: {
    searchTool,
  },
  memory: techSupportMemoryDemo,
})
