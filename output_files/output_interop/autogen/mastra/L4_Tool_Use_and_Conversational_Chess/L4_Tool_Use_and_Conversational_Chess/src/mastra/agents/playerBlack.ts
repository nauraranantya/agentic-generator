/**
 * Agent: Chess Player (Black)
 * ID: player_black
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Provides legal moves for the current chess position.
 *   - : Apply a move to the board and update board state; produce descriptive move result.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolGetLegalMoves, toolMakeMove } from '../tools'

/**
 * Chess Player (Black)
 * 
 * Instructions:
 * You are Chess Player (Black).
 */
export const playerBlack = new Agent({
  id: `player_black`,
  name: `Chess Player (Black)`,
  instructions: `You are Chess Player (Black).`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolGetLegalMoves,
    toolMakeMove,
  },
})
