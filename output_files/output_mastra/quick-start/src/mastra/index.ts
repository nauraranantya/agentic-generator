/**
 * Mastra AI Instance - Mastra
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { catOne } from './agents/catOne'

// Import workflows
import { logCatWorkflowPattern } from './workflows/logCatWorkflowPattern'
import { legacyLogCatWorkflowPattern } from './workflows/legacyLogCatWorkflowPattern'

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
