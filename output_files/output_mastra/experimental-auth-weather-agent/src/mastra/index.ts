/**
 * Mastra AI Instance - MastraServer/system
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { weatherAgent } from './agents/weatherAgent'

// Import workflows
import { weatherWorkflow } from './workflows/weatherWorkflow'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Represents the hosting Mastra system configuration for this agent/workflow deployment.
 */
export const mastra = new Mastra({
  agents: {
    weatherAgent,
  },
  workflows: {
    weatherWorkflow,
  },
})
