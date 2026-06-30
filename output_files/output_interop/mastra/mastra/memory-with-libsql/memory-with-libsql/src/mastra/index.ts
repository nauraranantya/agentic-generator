/**
 * Mastra AI Instance - MastraSystem
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { chefAgent, memoryAgent } from './agents'

// Import workflows
import { chefConversationPattern } from './workflows'

// Import memory instances
import { mastraMemory } from './memory'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Represents the Mastra multi-agent system constructed in the source code (mastra with two agents: chefAgent and memoryAgent).
 */
export const mastra = new Mastra({
  agents: {
    chefAgent,
    memoryAgent,
  },
  workflows: {
    chefConversationPattern,
  },
  memory: {
    mastraMemory,
  },
})
