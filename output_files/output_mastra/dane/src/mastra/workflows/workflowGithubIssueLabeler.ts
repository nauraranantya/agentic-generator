/**
 * Workflow: github-issue-labeler workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Fetch GitHub issue contents, obtain available labels, ask agent to select labels and apply them via GitHub integration.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'


// ── Workflow Definition ──

/**
 * github-issue-labeler workflow
 *
 * Fetch GitHub issue contents, obtain available labels, ask agent to select labels and apply them via GitHub integration.
 */
export const workflowGithubIssueLabeler = createWorkflow({
  id: 'github-issue-labeler workflow',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [],
})
  .commit()
