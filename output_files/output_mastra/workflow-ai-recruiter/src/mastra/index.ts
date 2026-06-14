/**
 * Mastra AI Instance - MastraProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { recruiterAgent } from './agents/recruiterAgent'

// Import workflows
import { candidateWorkflow } from './workflows/candidateWorkflow'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    recruiterAgent,
  },
  workflows: {
    candidateWorkflow,
  },
})
