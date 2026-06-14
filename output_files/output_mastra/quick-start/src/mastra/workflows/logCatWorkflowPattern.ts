/**
 * Workflow: log-cat-workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow that accepts an input { name: string } and runs a step to log the cat name, returning rawText. This corresponds to createWorkflow with id 'log-cat-workflow' in the source.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import tools used by workflow steps
import { consoleTool } from '../tools/consoleTool'

// ── Workflow Steps ──

const logCatNameStep = createStep({
  id: 'logCatName',
  description: `Workflow step that logs the 'name' input to console and returns rawText. The step expects inputSchema: { name: string } and produces outputSchema: { rawText: string }.`,
  inputSchema: z.object({ name: z.string() }),
  outputSchema: z.object({ rawText: z.string() }),
  execute: async ({ inputData }) => {
    // Task that takes { name: string } as input, performs logging 'Hello, <name> 🐈' and returns { rawText: string } containing the greeting. Implemented in source as createStep with id 'logCatName' and executed by the workflow runtime/console.
    // This step uses tool: consoleTool
    // TODO: Implement step logic
    throw new Error('logCatName not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * log-cat-workflow
 *
 * Workflow that accepts an input { name: string } and runs a step to log the cat name, returning rawText. This corresponds to createWorkflow with id 'log-cat-workflow' in the source.
 */
export const logCatWorkflowPattern = createWorkflow({
  id: 'log-cat-workflow',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [logCatNameStep],
})
  .then(logCatNameStep)
  .commit()
