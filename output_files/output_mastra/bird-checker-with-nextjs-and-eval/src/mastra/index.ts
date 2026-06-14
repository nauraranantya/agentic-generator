/**
 * Mastra AI Instance - MastraDeployment(birdChecker)
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
 * Deployment of the Bird Checker composed using Mastra: maps an agent id to a running LLM agent component.
 */
export const mastra = new Mastra({
  agents: {
    birdAgent,
  },
  workflows: {
    birdCheckerWorkflow,
  },
})
