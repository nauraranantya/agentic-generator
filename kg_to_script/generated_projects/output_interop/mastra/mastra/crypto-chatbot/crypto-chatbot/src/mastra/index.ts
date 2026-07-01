/**
 * Mastra AI Instance - Mastrasystem
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { cryptoAgent } from './agents'

// Import workflows
import { cryptoWorkflowPattern } from './workflows'

// Import memory instances
import { cryptoAgentMemory } from './memory'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    cryptoAgent,
  },
  workflows: {
    cryptoWorkflowPattern,
  },
  memory: {
    cryptoAgentMemory,
  },
})
