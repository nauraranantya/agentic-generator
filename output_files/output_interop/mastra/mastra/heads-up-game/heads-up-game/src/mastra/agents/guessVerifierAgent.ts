/**
 * Agent: verifier
 * ID: guess-verifier-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - Heads-Up game objective: Objective: run an interactive Heads-Up guessing game to let the user identify a famous person via yes/no questions and guesses.
 */

import { Agent } from '@mastra/core/agent'

/**
 * verifier
 * 
 * Instructions:
 * You are verifier.
 */
export const guessVerifierAgent = new Agent({
  id: `guess-verifier-agent`,
  name: `verifier`,
  instructions: `You are verifier.`,
  model: 'openai/gpt-4o-mini',
})
