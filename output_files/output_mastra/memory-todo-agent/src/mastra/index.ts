/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Objectives:
 *   - : Ensure tasks have an estimated duration to help with planning and prioritization.
 *   - : Guarantee that the user's todo list state is saved every interaction, per agent instruction.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { todoAgent } from './agents'

// Import workflows
import { todoChatLoop } from './workflows'

// Import memory instances
import { todoMemory } from './memory'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    todoAgent,
  },
  workflows: {
    todoChatLoop,
  },
  memory: {
    todoMemory,
  },
})
