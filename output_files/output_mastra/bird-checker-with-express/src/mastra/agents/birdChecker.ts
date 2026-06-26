/**
 * Agent: image-analyst
 * ID: bird-checker
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

/**
 * image-analyst
 * 
 * Instructions:
 * You are image-analyst.
 */
export const birdChecker = new Agent({
  id: `bird-checker`,
  name: `image-analyst`,
  instructions: `You are image-analyst.`,
  model: 'anthropic/claude-3-5-sonnet-latest',
})
