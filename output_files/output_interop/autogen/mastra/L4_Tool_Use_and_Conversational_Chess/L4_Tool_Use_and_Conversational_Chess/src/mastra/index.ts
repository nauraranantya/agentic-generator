/**
 * Mastra AI Instance - Chessplayersteam
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Environments:
 *   - Chess Environment (): 
 */

import { Mastra } from '@mastra/core'

// Import agents
import { playerWhite, playerBlack } from './agents'

// Import workflows
import { workflowPatternConversationalChess } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    playerWhite,
    playerBlack,
  },
  workflows: {
    workflowPatternConversationalChess,
  },
})
