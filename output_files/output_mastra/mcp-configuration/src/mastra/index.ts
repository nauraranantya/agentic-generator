/**
 * Mastra AI Instance - MastraExampleTeam/system
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { stockWeatherAgent } from './agents/stockWeatherAgent'

// Import workflows
import { stockWeatherWorkflow } from './workflows/stockWeatherWorkflow'

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
