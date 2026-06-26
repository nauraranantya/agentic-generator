/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { catOne } from './agents'

// Import workflows
import { logCatWorkflowPattern, legacyLogCatWorkflowPattern } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Agent orchestration system instance containing agents, workflows and logger configuration as defined in the source repository.
 */
export const mastra = new Mastra({
  agents: {
    catOne,
  },
  workflows: {
    logCatWorkflowPattern,
    legacyLogCatWorkflowPattern,
  },
})
