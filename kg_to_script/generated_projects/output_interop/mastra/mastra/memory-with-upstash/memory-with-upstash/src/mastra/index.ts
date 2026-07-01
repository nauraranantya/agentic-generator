/**
 * Mastra AI Instance - Mastrasystemagentorchestrator
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Improve user's cooking experience: 
 * Objectives:
 *   - Help user cook with available ingredients: Collective objective assigned to the Mastra system's agents to assist users in cooking with available ingredients.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { chefAgent, memoryAgent } from './agents'

// Import workflows
import { mastraConversationPattern } from './workflows'

// Import memory instances
import { sharedConversationMemory } from './memory'

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
    mastraConversationPattern,
  },
  memory: {
    sharedConversationMemory,
  },
})
