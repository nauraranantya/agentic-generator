/**
 * Workflow: message (entry) workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Interactive chat workflow: prompt user for message and then have dane agent respond (streaming or non-streaming).
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'


// ── Workflow Definition ──

/**
 * message (entry) workflow
 *
 * Interactive chat workflow: prompt user for message and then have dane agent respond (streaming or non-streaming).
 */
export const workflowMessage = createWorkflow({
  id: 'message (entry) workflow',
  inputSchema: z.object({Interactive_chat_workflow: z.string()}),
  outputSchema: z.object({}),
  steps: [],
})
  .commit()
