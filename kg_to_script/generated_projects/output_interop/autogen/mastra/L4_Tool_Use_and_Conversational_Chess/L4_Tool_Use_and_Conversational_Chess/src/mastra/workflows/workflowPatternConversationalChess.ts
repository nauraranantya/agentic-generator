/**
 * Workflow: Conversational Chess Workflow Pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import tools used by workflow steps
import { boardProxy } from '../tools'

// ── Workflow Steps ──

const taskInitiateChatBlackWhite = createStep({
  id: 'Task: Initiate chat (black -> white)',
  description: `Let's play chess! Your move.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Let's play chess! Your move.
    // TODO: Implement step logic
    throw new Error('Task: Initiate chat (black -> white) not implemented yet')
  },
})

const taskMakeMove = createStep({
  id: 'Task: Make move',
  description: `Call make_move(move) with a single move argument in UCI format when selecting a move to apply. Expect a textual confirmation describing the moved piece and board update.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Call make_move(move) with a single move argument in UCI format when selecting a move to apply. Expect a textual confirmation describing the moved piece and board update.
    // This step uses tool: boardProxy
    // TODO: Implement step logic
    throw new Error('Task: Make move not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * Conversational Chess Workflow Pattern
 */
export const workflowPatternConversationalChess = createWorkflow({
  id: 'Conversational Chess Workflow Pattern',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [taskInitiateChatBlackWhite, taskMakeMove],
})
  .then(taskInitiateChatBlackWhite)
  .then(taskMakeMove)
  .commit()
