/**
 * Agent: analyze images to detect birds, identify species and location
 * ID: bird-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - Accuracy evaluation objective: Objective to measure whether the agent identifies birds and species correctly (used by evaluation).
 * Capabilities:
 *   - analyze image (detect bird, species, location): Capability assigned to birdAgent: view image, determine if a bird is present, return species scientific name and a short human-readable location summary.
 *   - fetch random image from Unsplash: Tool capability: call Unsplash search API for a random image matching provided query and return a selected image object.
 */

import { Agent } from '@mastra/core/agent'

/**
 * analyze images to detect birds, identify species and location
 * 
 * Instructions:
 * agent instructions (default context for agent)
 */
export const birdAgent = new Agent({
  id: `bird-agent`,
  name: `analyze images to detect birds, identify species and location`,
  instructions: `agent instructions (default context for agent)`,
  model: 'anthropic/claude-3-haiku-20240307',
})
