/**
 * Agent: weather assistant
 * ID: weather-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import memory
import { weatherMemory } from '../memory'

/**
 * weather assistant
 * 
 * Instructions:
 * You are weather assistant.
 */
export const weatherAgent = new Agent({
  id: `weather-agent`,
  name: `weather assistant`,
  instructions: `You are weather assistant.`,
  model: 'openai/gpt-4o',
  memory: weatherMemory,
})
