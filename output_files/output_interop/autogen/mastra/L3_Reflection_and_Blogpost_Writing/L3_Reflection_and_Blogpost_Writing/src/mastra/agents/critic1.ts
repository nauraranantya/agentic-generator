/**
 * Agent: Critic
 * ID: critic-1
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : Objective: produce initial blogpost draft to be reviewed and refined.
 */

import { Agent } from '@mastra/core/agent'

/**
 * Critic
 * 
 * Instructions:
 * You are Critic.
 */
export const critic1 = new Agent({
  id: `critic-1`,
  name: `Critic`,
  instructions: `You are Critic.`,
  model: 'openai/gpt-4o-mini',
})
