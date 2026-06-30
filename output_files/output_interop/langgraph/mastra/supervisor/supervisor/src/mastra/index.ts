/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Provide assistance to user: 
 * Objectives:
 *   - Handle user query: 
 *   - Route selection: 
 */

import { Mastra } from '@mastra/core'

// Import agents
import { generativeUiSupervisor } from './agents'

// Import workflows
import { generativeUiWorkflow } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    generativeUiSupervisor,
  },
  workflows: {
    generativeUiWorkflow,
  },
})
