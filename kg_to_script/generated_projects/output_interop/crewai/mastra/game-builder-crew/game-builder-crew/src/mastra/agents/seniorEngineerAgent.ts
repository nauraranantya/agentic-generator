/**
 * Agent: Senior Software Engineer
 * ID: senior_engineer_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Web search and retrieval capability (e.g., Serper).
 *   - : Access to OpenAI language model API.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolSerper, toolOpenaiApi } from '../tools'

/**
 * Senior Software Engineer
 * 
 * Instructions:
 * Create software as needed
 */
export const seniorEngineerAgent = new Agent({
  id: `senior_engineer_agent`,
  name: `Senior Software Engineer`,
  instructions: `Create software as needed`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolSerper,
    toolOpenaiApi,
  },
})
