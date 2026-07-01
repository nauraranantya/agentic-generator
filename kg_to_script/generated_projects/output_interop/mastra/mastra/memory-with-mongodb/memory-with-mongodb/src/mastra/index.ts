/**
 * Mastra AI Instance - MastraSystem
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { chefAgent, memoryAgent } from './agents'

// Import memory instances
import { mastraMemory } from './memory'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    chefAgent,
    memoryAgent,
  },
  memory: {
    mastraMemory,
  },
})
