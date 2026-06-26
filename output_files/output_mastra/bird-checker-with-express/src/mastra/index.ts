/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { birdChecker } from './agents'

// Import workflows
import { imageMetadataWorkflow } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * The deployed Mastra-based system hosting an agent and tools to fetch and analyze images (server runs on Node/Express).
 */
export const mastra = new Mastra({
  agents: {
    birdChecker,
  },
  workflows: {
    imageMetadataWorkflow,
  },
})
