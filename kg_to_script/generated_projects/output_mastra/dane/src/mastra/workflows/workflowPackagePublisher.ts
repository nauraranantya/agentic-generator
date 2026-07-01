/**
 * Workflow: pnpm-changset-publisher
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Builds all packages, publishes changesets and sets dist-tags for monorepo packages.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'


// ── Workflow Definition ──

/**
 * pnpm-changset-publisher
 *
 * Builds all packages, publishes changesets and sets dist-tags for monorepo packages.
 */
export const workflowPackagePublisher = createWorkflow({
  id: 'pnpm-changset-publisher',
  inputSchema: z.object({publishes_changesets_and_sets_dist: z.string()}),
  outputSchema: z.object({}),
  steps: [],
})
  .commit()
