/**
 * Workflow: my-workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import tools used by workflow steps
import { mastraRuntime } from '../tools/mastraRuntime'

// Import nested sub-workflows
import { dataProcessing } from './dataProcessing'

// ── Workflow Steps ──

const invokeDataProcessingStep = createStep({
  id: 'invoke data-processing (nested workflow) step',
  inputSchema: z.object({ inputValue: z.number() }),
  outputSchema: z.object({ isEven: z.boolean() }),
  execute: async ({ inputData }) => {
    // Invokes nested workflow 'data-processing' with input schema { inputValue: number } and expects output { isEven: boolean }.
    // This step uses tool: mastraRuntime
    // TODO: Implement step logic
    throw new Error('invoke data-processing (nested workflow) step not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * my-workflow
 */
export const myWorkflow = createWorkflow({
  id: 'my-workflow',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [invokeDataProcessingStep],
})
  .then(invokeDataProcessingStep)
  .commit()
