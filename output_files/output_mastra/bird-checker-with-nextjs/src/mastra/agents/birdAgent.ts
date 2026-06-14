/**
 * Agent: Bird Checker agent
 * ID: bird-checker
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { getRandomImageTool } from '../tools/getRandomImageTool'

/**
 * Bird Checker agent
 * 
 * Instructions:
 * You can view an image and figure out if it is a bird or not. You can also figure out the species of the bird and where the picture was taken.
 */
export const birdAgent = new Agent({
  id: `bird-checker`,
  name: `Bird Checker agent`,
  instructions: `You can view an image and figure out if it is a bird or not. You can also figure out the species of the bird and where the picture was taken.`,
  model: 'anthropic/claude-3-haiku-20240307',
  tools: {
    getRandomImageTool,
  },
})
