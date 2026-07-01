/**
 * Workflow: markdown_validation_workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow pattern for the markdown validation crew (Process.sequential)
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { requirementsManager } from '../agents'

// ── Workflow Steps ──

const syntaxReviewTask = createStep({
  id: 'syntax_review_task',
  description: `Use the markdown_validation_tool to review the file(s) at this path: {filename}.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Use the markdown_validation_tool to review the file(s) at this path: {filename}.
    // This step uses agent: requirementsManager
    // const result = await requirementsManager.generate('...')
    // TODO: Implement step logic
    throw new Error('syntax_review_task not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * markdown_validation_workflow
 *
 * Workflow pattern for the markdown validation crew (Process.sequential)
 */
export const markdownValidationWorkflow = createWorkflow({
  id: 'markdown_validation_workflow',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [syntaxReviewTask],
})
  .parallel([syntaxReviewTask])
  .commit()
