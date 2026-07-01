/**
 * Workflow: workflow_custom_crew
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow inferred from Crew(..., tasks=[task_1_name, task_2_name]) ordering.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { agent1Name, agent2Name } from '../agents'

// ── Workflow Steps ──

const task1 = createStep({
  id: 'task_1',
  description: `Do something as part of task 1`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Do something as part of task 1
    // This step uses agent: agent1Name
    // const result = await agent1Name.generate('...')
    // TODO: Implement step logic
    throw new Error('task_1 not implemented yet')
  },
})

const task2 = createStep({
  id: 'task_2',
  description: `Take the input from task 1 and do something with it.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Take the input from task 1 and do something with it.
    // This step uses agent: agent2Name
    // const result = await agent2Name.generate('...')
    // TODO: Implement step logic
    throw new Error('task_2 not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * workflow_custom_crew
 *
 * Workflow inferred from Crew(..., tasks=[task_1_name, task_2_name]) ordering.
 */
export const workflowCustomCrew = createWorkflow({
  id: 'workflow_custom_crew',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [task1, task2],
})
  .then(task1)
  .then(task2)
  .commit()
