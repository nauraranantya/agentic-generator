/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { writerAnnotationAgentUuid1 } from './agents'

// Import workflows
import { writerWorkflow } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    writerAnnotationAgentUuid1,
  },
  workflows: {
    writerWorkflow,
  },
})
