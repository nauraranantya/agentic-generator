/**
 * Agent: Define agent 1 role here
 * ID: agent_1_name
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Performs web searches and returns results
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolDuckDuckGoSearchRun } from '../tools'

/**
 * Define agent 1 role here
 * 
 * Instructions:
 * Define agent 1 goal here
 */
export const agent1Name = new Agent({
  id: `agent_1_name`,
  name: `Define agent 1 role here`,
  instructions: `Define agent 1 goal here`,
  model: 'openai/gpt-3.5-turbo',
  tools: {
    toolDuckDuckGoSearchRun,
  },
})
