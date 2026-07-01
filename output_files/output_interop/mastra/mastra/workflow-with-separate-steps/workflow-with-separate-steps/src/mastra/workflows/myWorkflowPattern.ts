/**
 * Workflow: my_workflow_pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { mastraAgent } from '../agents'

// ── Workflow Steps ──

const taskStepOne = createStep({
  id: 'task_step_one',
  description: `Doubles triggerData.inputValue and returns an object with { doubledValue }.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Doubles triggerData.inputValue and returns an object with { doubledValue }.
    // This step uses agent: mastraAgent
    // const result = await mastraAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_step_one not implemented yet')
  },
})

const taskStepThree = createStep({
  id: 'task_step_three',
  description: `Triples triggerData.inputValue and returns an object with { tripledValue }.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Triples triggerData.inputValue and returns an object with { tripledValue }.
    // This step uses agent: mastraAgent
    // const result = await mastraAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_step_three not implemented yet')
  },
})

const taskStepTwo = createStep({
  id: 'task_step_two',
  description: `Reads the payload from stepOne (doubledValue) and returns an object with { incrementedValue } which is doubledValue + 1.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Reads the payload from stepOne (doubledValue) and returns an object with { incrementedValue } which is doubledValue + 1.
    // This step uses agent: mastraAgent
    // const result = await mastraAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_step_two not implemented yet')
  },
})

const taskStepFour = createStep({
  id: 'task_step_four',
  description: `Reads the payload from stepThree (tripledValue) and returns an object with { isEven } indicating whether tripledValue is even.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Reads the payload from stepThree (tripledValue) and returns an object with { isEven } indicating whether tripledValue is even.
    // This step uses agent: mastraAgent
    // const result = await mastraAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_step_four not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * my_workflow_pattern
 */
export const myWorkflowPattern = createWorkflow({
  id: 'my_workflow_pattern',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [taskStepOne, taskStepThree, taskStepTwo, taskStepFour],
})
  .then(taskStepOne)
  .then(taskStepThree)
  .then(taskStepTwo)
  .then(taskStepFour)
  .commit()
