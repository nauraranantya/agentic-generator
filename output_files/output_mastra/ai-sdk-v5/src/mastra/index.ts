/**
 * Mastra AI Instance - MastraProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { weatherAgent } from './agents/weatherAgent'

// Import memory instances
import { weatherAgentMemory } from './memory/weatherAgentMemory'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    weatherAgent,
  },
  memory: {
    weatherAgentMemory,
  },
})
