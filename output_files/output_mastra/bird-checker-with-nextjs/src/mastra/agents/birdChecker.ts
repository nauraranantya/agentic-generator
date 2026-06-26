/**
 * Agent: image analyst / bird identifier
 * ID: bird-checker
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - Acquire representative image for inspection: 
 *   - Identify bird presence/species and summarize location: 
 * Capabilities:
 *   - detect bird: Determine whether an image contains a bird (boolean).
 *   - identify species (scientific name): Identify the bird species, ideally returning scientific name as a string.
 *   - summarize location: Summarize the location of the photographed scene in one or two simple sentences.
 *   - fetch random image: Capability to query Unsplash and return a representative image resource.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { getRandomImageTool } from '../tools'

/**
 * image analyst / bird identifier
 * 
 * Instructions:
 * Agent instruction and purpose
 */
export const birdChecker = new Agent({
  id: `bird-checker`,
  name: `image analyst / bird identifier`,
  instructions: `Agent instruction and purpose`,
  model: 'anthropic/claude-3-haiku-20240307',
  tools: {
    getRandomImageTool,
  },
})
