/**
 * Agent: Board Proxy / Referee
 * ID: board_proxy
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Provides legal moves for the current chess position.
 *   - : Apply a move to the board and update board state; produce descriptive move result.
 */

import { Agent } from '@mastra/core/agent'

/**
 * Board Proxy / Referee
 * 
 * Instructions:
 * You are Board Proxy / Referee.
 */
export const boardProxy = new Agent({
  id: `board_proxy`,
  name: `Board Proxy / Referee`,
  instructions: `You are Board Proxy / Referee.`,
  model: 'openai/gpt-4o-mini',
})
