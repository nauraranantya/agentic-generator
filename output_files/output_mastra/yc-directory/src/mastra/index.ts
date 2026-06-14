/**
 * Mastra AI Instance - MastraSystem
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { ycDirectoryAgent } from './agents/ycDirectoryAgent'

// Import workflows
import { ycQueryWorkflow } from './workflows/ycQueryWorkflow'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * The Mastra system instance created in src/mastra/index.ts that composes agents and a logger.
 */
export const mastra = new Mastra({
  agents: {
    ycDirectoryAgent,
  },
  workflows: {
    ycQueryWorkflow,
  },
})
