/**
 * Agent: weather assistant
 * ID: Weather Agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Provide concise weather information including humidity, wind, precipitation; ask for location if not provided.
 *   - : Fetch current weather and geocoding for a given location using Open-Meteo APIs.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolGetWeather } from '../tools'

/**
 * weather assistant
 * 
 * Instructions:
 * You are weather assistant.
 */
export const weatherAgent = new Agent({
  id: `Weather Agent`,
  name: `weather assistant`,
  instructions: `You are weather assistant.`,
  model: 'openai/gpt-4o',
  tools: {
    toolGetWeather,
  },
})
