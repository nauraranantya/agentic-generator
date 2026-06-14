/**
 * Agent: Recruiter Agent
 * ID: recruiter-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

/**
 * Recruiter Agent
 * 
 * Instructions:
 * You are a recruiter.
 */
export const recruiterAgent = new Agent({
  id: `recruiter-agent`,
  name: `Recruiter Agent`,
  instructions: `You are a recruiter.`,
  model: 'openai/gpt-4o-mini',
})
