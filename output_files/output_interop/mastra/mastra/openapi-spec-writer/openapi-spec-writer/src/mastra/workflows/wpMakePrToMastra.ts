/**
 * Workflow: wp_make_pr_to_mastra
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow to format YAML, add files to GitHub and create a PR for the integration.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { openapiSpecGenAgent } from '../agents'

// Import tools used by workflow steps
import { toolAddToGithub } from '../tools'

// ── Workflow Steps ──

const taskAddToGithub = createStep({
  id: 'task_add_to_github',
  description: `Take a YAML blob, ask the agent to format it, then create branch, commit files and open a PR via the GitHub client.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Can you take this text blob and format it into proper YAML? Ensure valid OpenAPI syntax and remove surrounding code fences.
    // This step uses agent: openapiSpecGenAgent
    // const result = await openapiSpecGenAgent.generate('...')
    // This step uses tool: toolAddToGithub
    // TODO: Implement step logic
    throw new Error('task_add_to_github not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * wp_make_pr_to_mastra
 *
 * Workflow to format YAML, add files to GitHub and create a PR for the integration.
 */
export const wpMakePrToMastra = createWorkflow({
  id: 'wp_make_pr_to_mastra',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [taskAddToGithub],
})
  .then(taskAddToGithub)
  .commit()
