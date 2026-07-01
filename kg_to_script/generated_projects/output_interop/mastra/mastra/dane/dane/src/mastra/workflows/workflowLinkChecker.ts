/**
 * Workflow: workflow_link_checker
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { daneLinkChecker } from '../agents'

// ── Workflow Steps ──

const taskLinkGetBrokenLinks = createStep({
  id: 'task_link_get_broken_links',
  description: `Run linkinator via shell to collect links; parse JSON output`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Run linkinator via shell to collect links; parse JSON output
    // TODO: Implement step logic
    throw new Error('task_link_get_broken_links not implemented yet')
  },
})

const taskLinkReportBrokenLinks = createStep({
  id: 'task_link_report_broken_links',
  description: `Report broken links by generating a message with DaneLinkChecker and posting to Slack`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Format the broken links JSON into a human-friendly Slack message and send to the configured channel using slack_post_message tool.
    // This step uses agent: daneLinkChecker
    // const result = await daneLinkChecker.generate('...')
    // TODO: Implement step logic
    throw new Error('task_link_report_broken_links not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * workflow_link_checker
 */
export const workflowLinkChecker = createWorkflow({
  id: 'workflow_link_checker',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [taskLinkGetBrokenLinks, taskLinkReportBrokenLinks],
})
  .then(taskLinkGetBrokenLinks)
  .then(taskLinkReportBrokenLinks)
  .commit()
