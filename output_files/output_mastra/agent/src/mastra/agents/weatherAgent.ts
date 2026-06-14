/**
 * Agent: Weather Agent
 * ID: weather-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { weatherInfoTool } from '../tools/weatherInfoTool'

/**
 * Weather Agent
 * 
 */
export const weatherAgent = new Agent({
  id: `weather-agent`,
  name: `Weather Agent`,
  instructions: ``,
  model: 'openai/gpt-4o-mini',
  tools: {
    weatherInfoTool,
  },
})
