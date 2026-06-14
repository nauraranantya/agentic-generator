/**
 * Workflow: changelog workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Generates weekly changelogs by scanning a predefined list of module paths, computing diffs between two dates, and asking an agent to summarize per-module changes; posts combined changelog to Slack.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// ── Workflow Steps ──

const stepChangelogGetDiffs = createStep({
  id: 'stepA1',
  description: `Iterates modulePaths list, runs git diff between main@{weekAgo} and main@{today} for each module path; if diff non-empty, invokes daneChangeLog agent to produce a per-module changelog and writes to generated-changelogs/changelog-<today>.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Iterates modulePaths list, runs git diff between main@{weekAgo} and main@{today} for each module path; if diff non-empty, invokes daneChangeLog agent to produce a per-module changelog and writes to generated-changelogs/changelog-<today>.
    // TODO: Implement step logic
    throw new Error('stepA1 not implemented yet')
  },
})

const stepChangelogMakeChangelog = createStep({
  id: 'stepA2',
  description: `Combines per-module changelogs into a single narrative with sections (Opening, Major Updates, Technical Improvements, Documentation, Bug Fixes & Infrastructure), then sends to Slack channel using MCP Slack tool via daneChangeLog agent.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Combines per-module changelogs into a single narrative with sections (Opening, Major Updates, Technical Improvements, Documentation, Bug Fixes & Infrastructure), then sends to Slack channel using MCP Slack tool via daneChangeLog agent.
    // TODO: Implement step logic
    throw new Error('stepA2 not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * changelog workflow
 *
 * Generates weekly changelogs by scanning a predefined list of module paths, computing diffs between two dates, and asking an agent to summarize per-module changes; posts combined changelog to Slack.
 */
export const workflowChangelog = createWorkflow({
  id: 'changelog workflow',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [stepChangelogGetDiffs, stepChangelogMakeChangelog],
})
  .then(stepChangelogGetDiffs)
  .then(stepChangelogMakeChangelog)
  .commit()
