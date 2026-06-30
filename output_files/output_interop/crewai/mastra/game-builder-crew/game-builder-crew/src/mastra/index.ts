/**
 * Mastra AI Instance - GameBuilderCrew
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Create Game (Team Goal): Produce a working python game implementation given a textual game description input. The system assembles agents and tasks to generate, review, and evaluate final python code for a game (examples include Pac-Man and Snake).
 *   - Create software as needed: Create software as needed
 *   - Create Perfect code: Create Perfect code, by analyzing the code that is given for errors
 *   - Ensure the code does the job that it is supposed to do: Ensure that the code fulfills the functional requirements of the game description and is complete.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { seniorEngineerAgent, qaEngineerAgent, chiefQaEngineerAgent } from './agents'

// Import workflows
import { gameBuilderWorkflow } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    seniorEngineerAgent,
    qaEngineerAgent,
    chiefQaEngineerAgent,
  },
  workflows: {
    gameBuilderWorkflow,
  },
})
