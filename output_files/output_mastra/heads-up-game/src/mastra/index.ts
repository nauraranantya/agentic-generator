/**
 * Mastra AI Instance - Mastraagenticsystem
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Play Heads-Up Game: Top-level goal for the workflow/system: enable a complete game session and determine if the player guesses the famous person correctly.
 * Objectives:
 *   - Heads-Up game objective: Objective: run an interactive Heads-Up guessing game to let the user identify a famous person via yes/no questions and guesses.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { famousPersonGenerator, gameAgent, guessVerifierAgent } from './agents'

// Import workflows
import { headsUpWorkflow } from './workflows'

// Import memory instances
import { famousPersonMemory } from './memory'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Top-level system instance that composes agents, workflows, storage and logger used by the Heads-Up example.
 */
export const mastra = new Mastra({
  agents: {
    famousPersonGenerator,
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
