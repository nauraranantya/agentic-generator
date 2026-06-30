/**
 * Agent: Define agent 1 role here
 * ID: agent_1_name
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - web search: Capability to run web searches and return search results.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { duckDuckGoTool } from '../tools'

/**
 * Define agent 1 role here
 * 
 * Instructions:
 * agent settings: allow_delegation=False; verbose=True; llm=ChatOpenAI(gpt-3.5-turbo)
 */
export const agent1Name = new Agent({
  id: `agent_1_name`,
  name: `Define agent 1 role here`,
  instructions: `agent settings: allow_delegation=False; verbose=True; llm=ChatOpenAI(gpt-3.5-turbo)`,
  model: 'openai/gpt-3.5-turbo',
  tools: {
    duckDuckGoTool,
  },
})
