/**
 * Agent: Weather Assistant
 * ID: weather-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - HTTP fetch: Capability to perform HTTP requests to external APIs (used by the weather tool).
 *   - Text generation (LLM, streaming): Capability to generate natural language text and stream responses from a language model.
 *   - Get weather data: Capability to retrieve, parse and normalize weather information for a given location.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { weatherTool } from '../tools'

/**
 * Weather Assistant
 * 
 * Instructions:
 * You are Weather Assistant.
 */
export const weatherAgent = new Agent({
  id: `weather-agent`,
  name: `Weather Assistant`,
  instructions: `You are Weather Assistant.`,
  model: 'openai/gpt-4o',
  tools: {
    weatherTool,
  },
})
