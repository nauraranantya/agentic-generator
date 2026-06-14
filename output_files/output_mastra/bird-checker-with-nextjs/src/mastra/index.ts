/**
 * Mastra AI Instance - MastraProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { birdAgent } from './agents/birdAgent'

// Import workflows
import { birdCheckerWorkflow } from './workflows/birdCheckerWorkflow'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    birdAgent,
  },
  workflows: {
    birdCheckerWorkflow,
  },
})
