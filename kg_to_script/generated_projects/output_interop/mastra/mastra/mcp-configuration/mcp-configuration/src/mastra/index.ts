/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - : Goal representing the desired final state: a composed answer to the user that includes both current weather for requested location and current stock price for requested symbol.
 * Objectives:
 *   - : Objective grouping the sub-tasks needed to respond to the user (get weather, get stock price, compose reply).
 * Environments:
 *   -  (local): Describes the example execution environment where servers are spawned locally and an SSE endpoint is used for the weather tool.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { stockWeatherAgent } from './agents'

// Import workflows
import { stockWeatherWorkflow } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Conceptual team/system that contains the agent and the workflow pattern illustrating the runtime orchestration between the agent and tool servers.
 */
export const mastra = new Mastra({
  agents: {
    stockWeatherAgent,
  },
  workflows: {
    stockWeatherWorkflow,
  },
})
