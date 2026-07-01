/**
 * Agent: Chief Software Quality Control Engineer
 * ID: chief_qa_engineer_agent
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
 * Chief Software Quality Control Engineer
 * 
 * Instructions:
 * Ensure that the code does the job that it is supposed to do
 */
export const chiefQaEngineerAgent = new Agent({
  id: `chief_qa_engineer_agent`,
  name: `Chief Software Quality Control Engineer`,
  instructions: `Ensure that the code does the job that it is supposed to do`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolSerper,
    toolOpenaiApi,
  },
})
