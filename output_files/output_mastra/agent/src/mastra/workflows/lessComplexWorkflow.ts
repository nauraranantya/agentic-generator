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
import { chefModelV2Agent } from '../agents/chefModelV2Agent'
import { chefAgent } from '../agents/chefAgent'

// ── Workflow Steps ──

const stepAddLetter = createStep({
  id: 'add-letter',
  description: `Appends 'A' to input text. Input: { text: string }`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Execution: returns { text: text + 'A' } after ~500ms.
    // This step uses agent: chefModelV2Agent
    // const result = await chefModelV2Agent.generate('...')
    // TODO: Implement step logic
    throw new Error('add-letter not implemented yet')
  },
})

const stepAddLetterB = createStep({
  id: 'add-letter-b',
  description: `Appends 'B' to input text.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Execution: returns { text: text + 'B' }.
    // This step uses agent: chefModelV2Agent
    // const result = await chefModelV2Agent.generate('...')
    // TODO: Implement step logic
    throw new Error('add-letter-b not implemented yet')
  },
})

const stepAddLetterC = createStep({
  id: 'add-letter-c',
  description: `Appends 'C' to input text.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Execution: returns { text: text + 'C' }.
    // This step uses agent: chefModelV2Agent
    // const result = await chefModelV2Agent.generate('...')
    // TODO: Implement step logic
    throw new Error('add-letter-c not implemented yet')
  },
})

const stepAddLetterWithCount = createStep({
  id: 'add-letter-with-count',
  description: `Adds 'D' to text and increments iterationCount.`,
  inputSchema: z.object({}),
  outputSchema: z.object({ text: z.string(), iterationCount: z.number() }),
  execute: async ({ inputData }) => {
    // Execution: returns text + 'D' and iterationCount+1.
    // This step uses agent: chefModelV2Agent
    // const result = await chefModelV2Agent.generate('...')
    // TODO: Implement step logic
    throw new Error('add-letter-with-count not implemented yet')
  },
})

const stepSuspendResume = createStep({
  id: 'suspend-resume',
  description: `Suspend/resume step:`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData, suspend }) => {
    // Suspend/resume step
    // This step uses agent: chefAgent
    // Requires user input to resume. Modeled as a suspend/resume interactive step.
    // TODO: Check resume state and implement logic
    await suspend({
      message: 'Waiting for human input',
    })
    throw new Error('suspend-resume resume handler not implemented yet')
  },
})

const stepShortText = createStep({
  id: 'short-text',
  description: `Appends 'S' to short texts (branch target).`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Branch step executed when text length <= 10.
    // This step uses agent: chefModelV2Agent
    // const result = await chefModelV2Agent.generate('...')
    // TODO: Implement step logic
    throw new Error('short-text not implemented yet')
  },
})

const stepLongText = createStep({
  id: 'long-text',
  description: `Appends 'L' to long texts (branch target).`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Branch step executed when text length > 10.
    // This step uses agent: chefModelV2Agent
    // const result = await chefModelV2Agent.generate('...')
    // TODO: Implement step logic
    throw new Error('long-text not implemented yet')
  },
})

const stepNestedTextProcessor = createStep({
  id: 'nested-text-processor',
  description: `Nested workflow that runs add-letter then add-letter-b (see nestedTextProcessor workflow pattern below).`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Executes nested sub-workflow that appends letters A then B.
    // This step uses agent: chefModelV2Agent
    // const result = await chefModelV2Agent.generate('...')
    // TODO: Implement step logic
    throw new Error('nested-text-processor not implemented yet')
  },
})

const stepFinalStep = createStep({
  id: 'final-step',
  description: `Finalization step, appends '-ENDED' to the text.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Finalization operation adding '-ENDED'.
    // This step uses agent: chefAgent
    // const result = await chefAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('final-step not implemented yet')
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
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [stepAddLetter, stepAddLetterB, stepAddLetterC, stepAddLetterWithCount, stepSuspendResume, stepShortText, stepLongText, stepNestedTextProcessor, stepFinalStep],
})
  .then(stepAddLetter)
  .then(stepAddLetterB)
  .then(stepAddLetterC)
  .then(stepAddLetterWithCount)
  .then(stepSuspendResume)
  .then(stepShortText)
  .then(stepLongText)
  .then(stepNestedTextProcessor)
  .then(stepFinalStep)
  .commit()
