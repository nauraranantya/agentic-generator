/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Environments:
 *   -  (local-development): Configuration indicates use of localhost postgres and local services (from source code constants).
 */

import { Mastra } from '@mastra/core'

// Import agents
import { chefAgent, memoryAgent } from './agents'

// Import workflows
import { recipeWorkflowPattern, conversationWithMemoryPattern } from './workflows'

// Import memory instances
import { sharedMemoryStore } from './memory'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    chefAgent,
    memoryAgent,
  },
  workflows: {
    recipeWorkflowPattern,
    conversationWithMemoryPattern,
  },
  memory: {
    sharedMemoryStore,
  },
})
