/**
 * Agent: Weather assistant
 * ID: weather-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - fetch-current-weather: Capability to obtain current weather information for a specified location by calling geocoding and weather APIs and mapping the response to a structured output.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { getWeatherTool } from '../tools'

// Import memory
import { weatherAgentMemory } from '../memory'

/**
 * Weather assistant
 * 
 * Instructions:
 * You are Weather assistant.
 */
export const weatherAgent = new Agent({
  id: `weather-agent`,
  name: `Weather assistant`,
  instructions: `You are Weather assistant.`,
  model: 'openai/gpt-4o',
  tools: {
    getWeatherTool,
  },
  memory: weatherAgentMemory,
})
