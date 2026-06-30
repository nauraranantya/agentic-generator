/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import workflows
import { myWorkflowPattern } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Represents the Mastra deployment that contains the defined workflows.
 */
export const mastra = new Mastra({
  workflows: {
    myWorkflowPattern,
  },
})
