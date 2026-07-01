/**
 * Workflow: custom_crew_workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * A simple two-step workflow (StartStep -> EndStep) representing the Crew run in main.py.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { agent1Name, agent2Name } from '../agents'

// ── Workflow Steps ──

const task1 = createStep({
  id: 'Task 1',
  description: `Do something as part of task 1`,
  inputSchema: z.object({var1: z.string(), var2: z.string()}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Do something as part of task 1
    // This step uses agent: agent1Name
    // const result = await agent1Name.generate('...')
    // TODO: Implement step logic
    throw new Error('Task 1 not implemented yet')
  },
})

const task2 = createStep({
  id: 'Task 2',
  description: `Take the input from task 1 and do something with it.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Take the input from task 1 and do something with it.
    // This step uses agent: agent2Name
    // const result = await agent2Name.generate('...')
    // TODO: Implement step logic
    throw new Error('Task 2 not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * custom_crew_workflow
 *
 * A simple two-step workflow (StartStep -> EndStep) representing the Crew run in main.py.
 */
export const customCrewWorkflow = createWorkflow({
  id: 'custom_crew_workflow',
  inputSchema: z.object({A_simple_two: z.string()}),
  outputSchema: z.object({}),
  steps: [task1, task2],
})
  .parallel([task1, task2])
  .commit()
