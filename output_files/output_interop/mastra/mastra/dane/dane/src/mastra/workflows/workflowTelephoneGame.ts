/**
 * Workflow: telephoneGame workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Play a game of telephone: starts a message, passes it through participants with optional modification by an agent and supports suspension/resume awaiting user confirmation.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'


// ── Workflow Definition ──

/**
 * telephoneGame workflow
 *
 * Play a game of telephone: starts a message, passes it through participants with optional modification by an agent and supports suspension/resume awaiting user confirmation.
 */
export const workflowTelephoneGame = createWorkflow({
  id: 'telephoneGame workflow',
  inputSchema: z.object({Play_a_game_of_telephone: z.string()}),
  outputSchema: z.object({}),
  steps: [],
})
  .commit()
