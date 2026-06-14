/**
 * Mastra AI Instance - MastraApplicationSystem
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { weatherAgent } from './agents/weatherAgent'
import { planningAgent } from './agents/planningAgent'

// Import workflows
import { weatherWorkflow } from './workflows/weatherWorkflow'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Top-level application composition: registers weather workflow and the exported weather agent. Implementation used Mastra SDK to wire agents and workflows; that wiring is represented semantically here (agents + workflow membership).
 */
export const mastra = new Mastra({
  agents: {
    weatherAgent,
    planningAgent,
  },
  workflows: {
    weatherWorkflow,
  },
})
