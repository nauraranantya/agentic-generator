/**
 * Workflow: message (entry) workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Interactive chat workflow: prompt user for message and then have dane agent respond (streaming or non-streaming).
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// ── Workflow Steps ──

const stepMessageInput = createStep({
  id: 'message-input',
  description: `Prompts user for chat message (inquirer input) and ensures non-empty.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Prompts user for chat message (inquirer input) and ensures non-empty.
    // TODO: Implement step logic
    throw new Error('message-input not implemented yet')
  },
})

const stepMessageOutput = createStep({
  id: 'message-output',
  description: `Send user message to dane agent (stream or batch). Agent responds and output is printed. When streaming, chunks are emitted to stdout. Non-stream fallback uses dane.generate.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Send user message to dane agent (stream or batch). Agent responds and output is printed. When streaming, chunks are emitted to stdout. Non-stream fallback uses dane.generate.
    // TODO: Implement step logic
    throw new Error('message-output not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * message (entry) workflow
 *
 * Interactive chat workflow: prompt user for message and then have dane agent respond (streaming or non-streaming).
 */
export const workflowMessage = createWorkflow({
  id: 'message (entry) workflow',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [stepMessageInput, stepMessageOutput],
})
  .then(stepMessageInput)
  .then(stepMessageOutput)
  .commit()
