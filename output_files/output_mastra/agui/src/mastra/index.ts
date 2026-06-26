/**
 * Mastra AI Instance - MastraSystem
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { weatherAgent } from './agents'

// Import workflows
import { myNetworkPattern } from './workflows'

// Import memory instances
import { weatherMemory } from './memory'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    weatherAgent,
  },
  workflows: {
    myNetworkPattern,
  },
  memory: {
    weatherMemory,
  },
})
