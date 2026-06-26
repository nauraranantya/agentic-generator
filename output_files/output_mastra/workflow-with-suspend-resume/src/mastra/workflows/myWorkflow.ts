/**
 * Workflow: my-workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import tools used by workflow steps
import { mastraRuntime } from '../tools'

// Import nested sub-workflows
import { dataProcessing } from './dataProcessing'

// ── Workflow Steps ──

const invokeDataProcessingStep = createStep({
  id: 'Invoke nested data-processing workflow',
  description: `Invokes nested workflow 'data-processing' with input schema { inputValue: number } and expects output { isEven: boolean }.`,
  inputSchema: z.object({inputSchema: z.object({}), exampleInput: z.object({})}),
  outputSchema: z.object({outputSchema: z.object({})}),
  execute: async ({ inputData }) => {
    // Invokes nested workflow 'data-processing' with input schema { inputValue: number } and expects output { isEven: boolean }.
    // This step uses tool: mastraRuntime
    // TODO: Implement step logic
    throw new Error('Invoke nested data-processing workflow not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * my-workflow
 */
export const myWorkflow = createWorkflow({
  id: 'my-workflow',
  inputSchema: z.object({inputSchema: z.object({}), exampleInput: z.object({})}),
  outputSchema: z.object({outputSchema: z.object({})}),
  steps: [invokeDataProcessingStep],
})
  .parallel([invokeDataProcessingStep])
  .commit()
