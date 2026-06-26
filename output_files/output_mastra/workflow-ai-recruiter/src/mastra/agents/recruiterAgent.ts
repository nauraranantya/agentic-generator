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
 * Agent-level static instruction used as the recruiter's persona/instruction set for generation.
 */
export const recruiterAgent = new Agent({
  id: `recruiter-agent`,
  name: `Recruiter Agent`,
  instructions: `Agent-level static instruction used as the recruiter's persona/instruction set for generation.`,
  model: 'openai/gpt-4o-mini',
})
