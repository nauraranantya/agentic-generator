/**
 * Workflow: github-first-contributor-message workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * On first contributor PR, generate welcoming message combining PR title, body, diff and Mastra docs; post as PR comment.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'


// ── Workflow Definition ──

/**
 * github-first-contributor-message workflow
 *
 * On first contributor PR, generate welcoming message combining PR title, body, diff and Mastra docs; post as PR comment.
 */
export const workflowGithubFirstContributor = createWorkflow({
  id: 'github-first-contributor-message workflow',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [],
})
  .commit()
