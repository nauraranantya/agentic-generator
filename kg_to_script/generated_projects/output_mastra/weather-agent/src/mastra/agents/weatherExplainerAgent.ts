/**
 * Agent: LLM Agent
 * ID: weatherExplainerAgent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - Fetch current weather capability: Fetches geocoding for a city and retrieves current weather fields. Input: { location: string }. Output: { temperature, feelsLike, humidity, windSpeed, windGust, conditions, location }.
 */

import { Agent } from '@mastra/core/agent'

/**
 * LLM Agent
 * 
 * Instructions:
 * You are LLM Agent.
 */
export const weatherExplainerAgent = new Agent({
  id: `weatherExplainerAgent`,
  name: `LLM Agent`,
  instructions: `You are LLM Agent.`,
  model: 'openai/gpt-4o',
})
