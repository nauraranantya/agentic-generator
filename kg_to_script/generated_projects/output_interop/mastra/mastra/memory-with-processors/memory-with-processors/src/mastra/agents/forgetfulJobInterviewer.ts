/**
 * Agent: LLM Agent
 * ID: forgetful-job-interviewer
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import memory
import { forgetfulDemoMemory } from '../memory'

/**
 * LLM Agent
 * 
 * Instructions:
 * System instructions used during the interactive interviewer demo.
 */
export const forgetfulJobInterviewer = new Agent({
  id: `forgetful-job-interviewer`,
  name: `LLM Agent`,
  instructions: `System instructions used during the interactive interviewer demo.`,
  model: 'openai/gpt-4o',
  memory: forgetfulDemoMemory,
})
