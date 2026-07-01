/**
 * Agent: LLM Agent
 * ID: forgetful-job-interviewer-repo
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { searchTool } from '../tools'

// Import memory
import { interviewMemoryRepo } from '../memory'

/**
 * LLM Agent
 * 
 * Instructions:
 * System instructions used in repository example (mastra/agents).
 */
export const forgetfulJobInterviewerRepo = new Agent({
  id: `forgetful-job-interviewer-repo`,
  name: `LLM Agent`,
  instructions: `System instructions used in repository example (mastra/agents).`,
  model: 'openai/gpt-4o',
  tools: {
    searchTool,
  },
  memory: interviewMemoryRepo,
})
