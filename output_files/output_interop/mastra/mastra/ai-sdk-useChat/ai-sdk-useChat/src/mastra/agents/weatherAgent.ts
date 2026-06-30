/**
 * Agent: weather assistant
 * ID: weather-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - get weather capability: Capability to obtain current weather information for a given location (geocoding + weather API calls, returns normalized weather fields).
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { getWeatherTool } from '../tools'

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
  model: 'anthropic/claude-3-5-sonnet-20241022',
  tools: {
    getWeatherTool,
  },
})
