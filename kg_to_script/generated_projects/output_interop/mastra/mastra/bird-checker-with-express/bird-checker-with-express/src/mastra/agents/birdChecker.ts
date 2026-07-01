/**
 * Agent: bird-checker
 * ID: Bird checker
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Classify images as bird/non-bird, identify species, and summarize location.
 *   - : Search Unsplash and return a random image matching a query (returns imageUrl, photographerName, photographerProfile).
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { getRandomImageTool } from '../tools'

/**
 * bird-checker
 * 
 * Instructions:
 * Determine whether an image contains a bird, identify the species, and summarize the location.
 */
export const birdChecker = new Agent({
  id: `Bird checker`,
  name: `bird-checker`,
  instructions: `Determine whether an image contains a bird, identify the species, and summarize the location.`,
  model: 'anthropic/claude-3-5-sonnet-latest',
  tools: {
    getRandomImageTool,
  },
})
