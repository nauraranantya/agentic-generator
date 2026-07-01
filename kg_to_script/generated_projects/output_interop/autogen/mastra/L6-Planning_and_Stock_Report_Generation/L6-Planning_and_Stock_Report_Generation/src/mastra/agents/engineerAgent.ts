/**
 * Agent: Engineer
 * ID: engineerAgent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : 
 */

import { Agent } from '@mastra/core/agent'

/**
 * Engineer
 * 
 * Instructions:
 * Engineer: writes code per planner's plan
 */
export const engineerAgent = new Agent({
  id: `engineerAgent`,
  name: `Engineer`,
  instructions: `Engineer: writes code per planner's plan`,
  model: 'openai/gpt-4-turbo',
})
