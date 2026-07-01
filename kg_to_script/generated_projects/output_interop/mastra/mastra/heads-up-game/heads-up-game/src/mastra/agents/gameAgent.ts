/**
 * Agent: game-assistant
 * ID: game-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - Heads-Up game objective: Objective: run an interactive Heads-Up guessing game to let the user identify a famous person via yes/no questions and guesses.
 */

import { Agent } from '@mastra/core/agent'

/**
 * game-assistant
 * 
 * Instructions:
 * Agent instructions and required structured JSON output (response, gameWon).
 */
export const gameAgent = new Agent({
  id: `game-agent`,
  name: `game-assistant`,
  instructions: `Agent instructions and required structured JSON output (response, gameWon).`,
  model: 'openai/gpt-4o',
})
