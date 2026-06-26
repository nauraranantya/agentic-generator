/**
 * Workflow: my-workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow that wraps the nested data-processing workflow.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import nested sub-workflows
import { nestedWorkflow } from './nestedWorkflow'


// ── Workflow Definition ──

/**
 * my-workflow
 *
 * Workflow that wraps the nested data-processing workflow.
 */
export const myWorkflowX = createWorkflow({
  id: 'my-workflow',
  inputSchema: z.object({Workflow_that_wraps_the_nested_data: z.string()}),
  outputSchema: z.object({}),
  steps: [],
})
  .commit()
