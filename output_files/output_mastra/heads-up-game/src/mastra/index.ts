/**
 * Mastra AI Instance - Mastra(agenticSystem)
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { famousPersonAgent } from './agents/famousPersonAgent'
import { gameAgent } from './agents/gameAgent'
import { guessVerifierAgent } from './agents/guessVerifierAgent'

// Import workflows
import { headsUpWorkflow } from './workflows/headsUpWorkflow'

// Import memory instances
import { famousPersonMemory } from './memory/famousPersonMemory'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Top-level system instance that composes agents, workflows, storage and logger used by the Heads-Up example.
 */
export const mastra = new Mastra({
  agents: {
    famousPersonAgent,
    gameAgent,
    guessVerifierAgent,
  },
  workflows: {
    headsUpWorkflow,
  },
  memory: {
    famousPersonMemory,
  },
})
