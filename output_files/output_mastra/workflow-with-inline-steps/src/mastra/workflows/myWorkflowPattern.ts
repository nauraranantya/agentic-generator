/**
 * Workflow: my-workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow defined in src/mastra/workflows/index.ts with a numeric trigger schema { inputValue: number }. Steps: stepOne -> stepTwo -> stepThree. Committed (myWorkflow.commit()).
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import tools used by workflow steps
import { mastraEngineTool } from '../tools/mastraEngineTool'

// ── Workflow Steps ──

const stepOneStep = createStep({
  id: 'stepOne',
  description: `Start step that doubles the workflow trigger input.`,
  inputSchema: z.object({ value: z.number() }),
  outputSchema: z.object({ doubledValue: z.number() }),
  execute: async ({ inputData }) => {
    // Execution logic (preserved from source):
    // This step uses tool: mastraEngineTool
    // TODO: Implement step logic
    throw new Error('stepOne not implemented yet')
  },
})

const stepTwoStep = createStep({
  id: 'stepTwo',
  description: `Second step increments a provided numeric value by 1. Expectation: receives a value under input key 'valueToIncrement'.`,
  inputSchema: z.object({ valueToIncrement: z.number() }),
  outputSchema: z.object({ incrementedValue: z.number() }),
  execute: async ({ inputData }) => {
    // Execution logic (preserved from source):
    // This step uses tool: mastraEngineTool
    // TODO: Implement step logic
    throw new Error('stepTwo not implemented yet')
  },
})

const stepThreeStep = createStep({
  id: 'stepThree',
  description: `Final step: may suspend workflow for confirmation, otherwise returns a thank-you message.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Execution logic (preserved from source):
    // This step uses tool: mastraEngineTool
    // TODO: Implement step logic
    throw new Error('stepThree not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * my-workflow
 *
 * Workflow defined in src/mastra/workflows/index.ts with a numeric trigger schema { inputValue: number }. Steps: stepOne -> stepTwo -> stepThree. Committed (myWorkflow.commit()).
 */
export const myWorkflowPattern = createWorkflow({
  id: 'my-workflow',
  inputSchema: z.object({ inputValue: z.number() }),
  outputSchema: z.object({}),
  steps: [stepOneStep, stepTwoStep, stepThreeStep],
})
  .then(stepOneStep)
  .then(stepTwoStep)
  .then(stepThreeStep)
  .commit()
