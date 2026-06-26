/**
 * Workflow: lessComplexWorkflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Complex workflow that:
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { chefModelV2Agent, chefAgent } from '../agents'

// ── Workflow Steps ──

const stepAddLetter = createStep({
  id: 'task:add-letter',
  description: `Execution: returns { text: text + 'A' } after ~500ms.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Execution: returns { text: text + 'A' } after ~500ms.
    // This step uses agent: chefModelV2Agent
    // const result = await chefModelV2Agent.generate('...')
    // TODO: Implement step logic
    throw new Error('task:add-letter not implemented yet')
  },
})

const stepAddLetterB = createStep({
  id: 'task:add-letter-b',
  description: `Execution: returns { text: text + 'B' }.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Execution: returns { text: text + 'B' }.
    // This step uses agent: chefModelV2Agent
    // const result = await chefModelV2Agent.generate('...')
    // TODO: Implement step logic
    throw new Error('task:add-letter-b not implemented yet')
  },
})

const stepAddLetterC = createStep({
  id: 'task:add-letter-c',
  description: `Execution: returns { text: text + 'C' }.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Execution: returns { text: text + 'C' }.
    // This step uses agent: chefModelV2Agent
    // const result = await chefModelV2Agent.generate('...')
    // TODO: Implement step logic
    throw new Error('task:add-letter-c not implemented yet')
  },
})

const stepAddLetterWithCount = createStep({
  id: 'task:add-letter-with-count',
  description: `Execution: returns text + 'D' and iterationCount+1.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Execution: returns text + 'D' and iterationCount+1.
    // This step uses agent: chefModelV2Agent
    // const result = await chefModelV2Agent.generate('...')
    // TODO: Implement step logic
    throw new Error('task:add-letter-with-count not implemented yet')
  },
})

const stepSuspendResume = createStep({
  id: 'task:suspend-resume',
  description: `Requires user input to resume. Modeled as a suspend/resume interactive step.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Requires user input to resume. Modeled as a suspend/resume interactive step.
    // This step uses agent: chefAgent
    // const result = await chefAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task:suspend-resume not implemented yet')
  },
})

const stepShortText = createStep({
  id: 'task:short-text',
  description: `Branch step executed when text length <= 10.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Branch step executed when text length <= 10.
    // This step uses agent: chefModelV2Agent
    // const result = await chefModelV2Agent.generate('...')
    // TODO: Implement step logic
    throw new Error('task:short-text not implemented yet')
  },
})

const stepLongText = createStep({
  id: 'task:long-text',
  description: `Branch step executed when text length > 10.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Branch step executed when text length > 10.
    // This step uses agent: chefModelV2Agent
    // const result = await chefModelV2Agent.generate('...')
    // TODO: Implement step logic
    throw new Error('task:long-text not implemented yet')
  },
})

const stepNestedTextProcessor = createStep({
  id: 'task:nested-text-processor',
  description: `Executes nested sub-workflow that appends letters A then B.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Executes nested sub-workflow that appends letters A then B.
    // This step uses agent: chefModelV2Agent
    // const result = await chefModelV2Agent.generate('...')
    // TODO: Implement step logic
    throw new Error('task:nested-text-processor not implemented yet')
  },
})

const stepFinalStep = createStep({
  id: 'task:final-step',
  description: `Finalization operation adding '-ENDED'.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Finalization operation adding '-ENDED'.
    // This step uses agent: chefAgent
    // const result = await chefAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task:final-step not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * lessComplexWorkflow
 *
 * Complex workflow that:
 */
export const lessComplexWorkflow = createWorkflow({
  id: 'lessComplexWorkflow',
  inputSchema: z.object({Runs_add: z.string(), add_letter: z.string(), short_text_vs_long: z.string(), Loops_with_add_letter_with: z.string(), Presents_suspend: z.string(), Runs_final: z.string(), Output: z.string()}),
  outputSchema: z.object({}),
  steps: [stepAddLetter, stepAddLetterB, stepAddLetterC, stepAddLetterWithCount, stepSuspendResume, stepShortText, stepLongText, stepNestedTextProcessor, stepFinalStep],
})
  .parallel([stepAddLetter, stepAddLetterB, stepAddLetterC, stepAddLetterWithCount, stepSuspendResume, stepShortText, stepLongText, stepNestedTextProcessor, stepFinalStep])
  .commit()
