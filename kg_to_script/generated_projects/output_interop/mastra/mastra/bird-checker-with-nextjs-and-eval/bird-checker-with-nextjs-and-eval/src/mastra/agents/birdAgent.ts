/**
 * Agent: bird classifier
 * ID: birdAgent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Fetch a random image from Unsplash matching the given query (wildlife | feathers | flying | birds).
 */

import { Agent } from '@mastra/core/agent'

/**
 * bird classifier
 * 
 * Instructions:
 * System should determine whether a provided image contains a bird, identify its scientific name if present, and summarize location.
 */
export const birdAgent = new Agent({
  id: `birdAgent`,
  name: `bird classifier`,
  instructions: `System should determine whether a provided image contains a bird, identify its scientific name if present, and summarize location.`,
  model: 'anthropic/claude-3-5-sonnet-latest',
})
