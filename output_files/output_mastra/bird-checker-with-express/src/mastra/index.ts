/**
 * Mastra AI Instance - MastraServer
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { birdCheckerAgent } from './agents/birdCheckerAgent'

// Import workflows
import { imageMetadataWorkflow } from './workflows/imageMetadataWorkflow'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * The deployed Mastra-based system hosting an agent and tools to fetch and analyze images (server runs on Node/Express).
 */
export const mastra = new Mastra({
  agents: {
    birdCheckerAgent,
  },
  workflows: {
    imageMetadataWorkflow,
  },
})
