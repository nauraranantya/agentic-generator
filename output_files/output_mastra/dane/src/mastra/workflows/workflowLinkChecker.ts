/**
 * Workflow: link-checker workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Checks a target URL for broken links using linkinator and posts results to Slack via MCP.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'


// ── Workflow Definition ──

/**
 * link-checker workflow
 *
 * Checks a target URL for broken links using linkinator and posts results to Slack via MCP.
 */
export const workflowLinkChecker = createWorkflow({
  id: 'link-checker workflow',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [],
})
  .commit()
