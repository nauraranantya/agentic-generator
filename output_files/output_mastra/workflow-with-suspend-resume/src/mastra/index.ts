/**
 * Mastra AI Instance - MastraSystem
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import workflows
import { myWorkflow } from './workflows/myWorkflow'
import { dataProcessing } from './workflows/dataProcessing'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  workflows: {
    myWorkflow,
    dataProcessing,
  },
})
