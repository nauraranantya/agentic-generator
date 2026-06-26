/**
 * Agent: LLM Agent
 * ID: planning-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - get weather capability: Capability to obtain current weather information for a given location (geocoding + weather API calls, returns normalized weather fields).
 */

import { Agent } from '@mastra/core/agent'

/**
 * LLM Agent
 * 
 * Instructions:
 * You are LLM Agent.
 */
export const planningAgent = new Agent({
  id: `planning-agent`,
  name: `LLM Agent`,
  instructions: `You are LLM Agent.`,
  model: 'anthropic/claude-3-5-sonnet-20241022',
})
