/**
 * Agent: black
 * ID: player_black
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - Play chess: General capability to select and execute chess moves.
 *   - Request legal moves: Capability to request the current legal moves from the board.
 *   - Make move: Capability to request the board to apply a move in UCI format and update the board state.
 */

import { Agent } from '@mastra/core/agent'

/**
 * black
 * 
 * Instructions:
 * You are black.
 */
export const playerBlack = new Agent({
  id: `player_black`,
  name: `black`,
  instructions: `You are black.`,
  model: 'openai/gpt-4o-mini',
})
