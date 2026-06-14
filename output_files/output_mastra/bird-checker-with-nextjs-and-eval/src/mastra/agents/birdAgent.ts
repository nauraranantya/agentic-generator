/**
 * Agent: Bird Agent
 * ID: bird-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

/**
 * Bird Agent
 * 
 * Instructions:
 * You can view an image and figure out if it is a bird or not. You can also figure out the species of the bird and where the picture was taken.
 */
export const birdAgent = new Agent({
  id: `bird-agent`,
  name: `Bird Agent`,
  instructions: `You can view an image and figure out if it is a bird or not. You can also figure out the species of the bird and where the picture was taken.`,
  model: 'anthropic/claude-3-haiku-20240307',
})
