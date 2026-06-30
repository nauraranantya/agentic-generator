/**
 * Agent: white
 * ID: player_white
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - Play chess: General capability to select and execute chess moves.
 *   - Request legal moves: Capability to request the current legal moves from the board.
 *   - Make move: Capability to request the board to apply a move in UCI format and update the board state.
 */

import { Agent } from '@mastra/core/agent'

/**
 * white
 * 
 * Instructions:
 * You are white.
 */
export const playerWhite = new Agent({
  id: `player_white`,
  name: `white`,
  instructions: `You are white.`,
  model: 'openai/gpt-4o-mini',
})
