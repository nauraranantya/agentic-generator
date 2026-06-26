/**
 * Agent: weather assistant
 * ID: weather-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - Fetch current weather capability: Fetches geocoding for a city and retrieves current weather fields. Input: { location: string }. Output: { temperature, feelsLike, humidity, windSpeed, windGust, conditions, location }.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { weatherTool } from '../tools'

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
  model: 'openai/gpt-4o-mini',
  tools: {
    weatherTool,
  },
})
