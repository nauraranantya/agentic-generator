/**
 * Agent: Chess Player (White)
 * ID: player_white
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
 * Chess Player (White)
 * 
 * Instructions:
 * You are Chess Player (White).
 */
export const playerWhite = new Agent({
  id: `player_white`,
  name: `Chess Player (White)`,
  instructions: `You are Chess Player (White).`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolGetLegalMoves,
    toolMakeMove,
  },
})
