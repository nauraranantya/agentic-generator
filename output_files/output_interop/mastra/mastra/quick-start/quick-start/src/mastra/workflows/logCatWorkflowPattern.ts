/**
 * Workflow: log_cat_workflow_pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow that accepts an input { name: string } and runs a step to log the cat name, returning rawText. This corresponds to createWorkflow with id 'log-cat-workflow' in the source.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import tools used by workflow steps
import { consoleTool } from '../tools'

// ── Workflow Steps ──

const taskLogCatName = createStep({
  id: 'task_log_cat_name',
  description: `Task that takes { name: string } as input, performs logging 'Hello, <name> 🐈' and returns { rawText: string } containing the greeting. Implemented in source as createStep with id 'logCatName' and executed by the workflow runtime/console.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Task that takes { name: string } as input, performs logging 'Hello, <name> 🐈' and returns { rawText: string } containing the greeting. Implemented in source as createStep with id 'logCatName' and executed by the workflow runtime/console.
    // This step uses tool: consoleTool
    // TODO: Implement step logic
    throw new Error('task_log_cat_name not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * log_cat_workflow_pattern
 *
 * Workflow that accepts an input { name: string } and runs a step to log the cat name, returning rawText. This corresponds to createWorkflow with id 'log-cat-workflow' in the source.
 */
export const logCatWorkflowPattern = createWorkflow({
  id: 'log_cat_workflow_pattern',
  inputSchema: z.object({name: z.string()}),
  outputSchema: z.object({}),
  steps: [taskLogCatName],
})
  .then(taskLogCatName)
  .commit()
