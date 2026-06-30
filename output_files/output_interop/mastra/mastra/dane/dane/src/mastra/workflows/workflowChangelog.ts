/**
 * Workflow: changelog workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Generates weekly changelogs by scanning a predefined list of module paths, computing diffs between two dates, and asking an agent to summarize per-module changes; posts combined changelog to Slack.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'


// ── Workflow Definition ──

/**
 * changelog workflow
 *
 * Generates weekly changelogs by scanning a predefined list of module paths, computing diffs between two dates, and asking an agent to summarize per-module changes; posts combined changelog to Slack.
 */
export const workflowChangelog = createWorkflow({
  id: 'changelog workflow',
  inputSchema: z.object({and_asking_an_agent_to_summarize_per: z.string()}),
  outputSchema: z.object({}),
  steps: [],
})
  .commit()
