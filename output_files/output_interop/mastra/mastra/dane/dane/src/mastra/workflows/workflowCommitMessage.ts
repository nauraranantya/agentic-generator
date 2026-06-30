/**
 * Workflow: commit-message workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow to generate and optionally commit a sensible git commit message for staged changes.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'


// ── Workflow Definition ──

/**
 * commit-message workflow
 *
 * Workflow to generate and optionally commit a sensible git commit message for staged changes.
 */
export const workflowCommitMessage = createWorkflow({
  id: 'commit-message workflow',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [],
})
  .commit()
