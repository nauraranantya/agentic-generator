/**
 * Workflow: wp_stategraph
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { chatAgent } from '../agents'

// ── Workflow Steps ──

const taskChat = createStep({
  id: 'task_chat',
  description: `Invoke model with the system prompt and current state.messages; return response messages.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Invoke model with the system prompt and current state.messages; return response messages.
    // This step uses agent: chatAgent
    // const result = await chatAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_chat not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * wp_stategraph
 */
export const wpStategraph = createWorkflow({
  id: 'wp_stategraph',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [taskChat],
})
  .parallel([taskChat])
  .commit()
