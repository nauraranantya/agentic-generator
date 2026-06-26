/**
 * Mastra AI Instance - MastraSystem
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { weatherAgent, weatherExplainerAgent } from './agents'

// Import workflows
import { wfWeatherWorkflow, wfWeatherWorkflowWithToolAndAgent } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * System coordinating weather agents, tools and workflows (Mastra instance configured with LibSQL storage and multiple workflows).
 */
export const mastra = new Mastra({
  agents: {
    weatherAgent,
    weatherExplainerAgent,
  },
  workflows: {
    wfWeatherWorkflow,
    wfWeatherWorkflowWithToolAndAgent,
  },
})
