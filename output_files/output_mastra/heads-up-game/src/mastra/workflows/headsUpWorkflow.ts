/**
 * Workflow: heads-up-workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow that implements the Heads-Up guessing game. The workflow: start-step -> repeated game-step until gameWon -> win-step. The 'do until' loop must be interpreted by the runtime as: repeat game-step until the 'gameWon' output becomes true.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { famousPersonAgent } from '../agents/famousPersonAgent'
import { gameAgent } from '../agents/gameAgent'

// ── Workflow Steps ──

const startWorkflowStep = createStep({
  id: 'start-step',
  description: `Initial step that requests generation of a famous person's name and initializes guessCount to 0.`,
  inputSchema: z.object({}),
  outputSchema: z.object({ famousPerson: z.string(), guessCount: z.any() }),
  execute: async ({ inputData }) => {
    // Generate a famous person's name
    // This step uses agent: famousPersonAgent
    // const result = await famousPersonAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('start-step not implemented yet')
  },
})

const gameWorkflowStep = createStep({
  id: 'game-step',
  description: `Main interactive loop step. Behavior:`,
  inputSchema: z.object({}),
  outputSchema: z.object({ response: z.string(), gameWon: z.boolean() }),
  execute: async ({ inputData }) => {
    // The famous person is: \${famousPerson}
    // This step uses agent: gameAgent
    // const result = await gameAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('game-step not implemented yet')
  },
})

const winWorkflowStep = createStep({
  id: 'win-step',
  description: `Final step that handles game-win logic (logging/returning final outputs).`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Finalization task:
    // TODO: Implement step logic
    throw new Error('win-step not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * heads-up-workflow
 *
 * Workflow that implements the Heads-Up guessing game. The workflow: start-step -> repeated game-step until gameWon -> win-step. The 'do until' loop must be interpreted by the runtime as: repeat game-step until the 'gameWon' output becomes true.
 */
export const headsUpWorkflow = createWorkflow({
  id: 'heads-up-workflow',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [startWorkflowStep, gameWorkflowStep, winWorkflowStep],
})
  .then(startWorkflowStep)
  .then(gameWorkflowStep)
  .then(winWorkflowStep)
  .commit()
