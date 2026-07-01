/**
 * Agent: Software Quality Control Engineer
 * ID: qa_engineer_agent
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
 * Software Quality Control Engineer
 * 
 * Instructions:
 * Create Perfect code, by analyzing the code that is given for errors
 */
export const qaEngineerAgent = new Agent({
  id: `qa_engineer_agent`,
  name: `Software Quality Control Engineer`,
  instructions: `Create Perfect code, by analyzing the code that is given for errors`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolSerper,
    toolOpenaiApi,
  },
})
