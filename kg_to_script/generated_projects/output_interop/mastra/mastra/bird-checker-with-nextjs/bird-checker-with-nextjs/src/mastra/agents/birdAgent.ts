/**
 * Agent: Bird checker
 * ID: birdAgent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Fetch random image matching a query from the Unsplash API
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { getRandomImageTool } from '../tools'

/**
 * Bird checker
 * 
 * Instructions:
 * Identify if an image depicts a bird, provide the scientific name if it is a bird, and summarize the image location in one or two short sentences.
 */
export const birdAgent = new Agent({
  id: `birdAgent`,
  name: `Bird checker`,
  instructions: `Identify if an image depicts a bird, provide the scientific name if it is a bird, and summarize the image location in one or two short sentences.`,
  model: 'anthropic/claude-3-5-sonnet-latest',
  tools: {
    getRandomImageTool,
  },
})
