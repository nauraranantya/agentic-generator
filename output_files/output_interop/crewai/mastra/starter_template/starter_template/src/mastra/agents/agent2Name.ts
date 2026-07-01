/**
 * Agent: Define agent 2 role here
 * ID: agent_2_name
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Performs web searches and returns results
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolDuckDuckGoSearchRun } from '../tools'

/**
 * Define agent 2 role here
 * 
 * Instructions:
 * Define agent 2 goal here
 */
export const agent2Name = new Agent({
  id: `agent_2_name`,
  name: `Define agent 2 role here`,
  instructions: `Define agent 2 goal here`,
  model: 'openai/gpt-3.5-turbo',
  tools: {
    toolDuckDuckGoSearchRun,
  },
})
