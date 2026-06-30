/**
 * Agent: Requirements Manager
 * ID: Requirements_Manager
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { markdownValidationTool } from '../tools'

/**
 * Requirements Manager
 * 
 * Instructions:
 * Agent backstory: expert business analyst and software QA specialist.
 */
export const requirementsManager = new Agent({
  id: `Requirements_Manager`,
  name: `Requirements Manager`,
  instructions: `Agent backstory: expert business analyst and software QA specialist.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    markdownValidationTool,
  },
})
