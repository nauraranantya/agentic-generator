/**
 * Workflow: screenplay_creation_sequential
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow pattern that sequentially runs analysis, scriptwriting, and formatting tasks, passing output to the next step.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { analyst, scriptwriter, formatter } from '../agents'

// ── Workflow Steps ──

const task1Analysis = createStep({
  id: 'task1: analysis',
  description: `Analyse in much detail the following discussion:`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Analyse in much detail the following discussion:
    // This step uses agent: analyst
    // const result = await analyst.generate('...')
    // TODO: Implement step logic
    throw new Error('task1: analysis not implemented yet')
  },
})

const task2Scriptwriting = createStep({
  id: 'task2: scriptwriting',
  description: `Create a dialogue heavy screenplay from the discussion, between two persons. Do NOT write parentheticals. Leave out wrylies. You MUST SKIP directional notes.`,
  inputSchema: z.object({Input_should_be_the_analysis_output_from: z.string()}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Create a dialogue heavy screenplay from the discussion, between two persons. Do NOT write parentheticals. Leave out wrylies. You MUST SKIP directional notes.
    // This step uses agent: scriptwriter
    // const result = await scriptwriter.generate('...')
    // TODO: Implement step logic
    throw new Error('task2: scriptwriting not implemented yet')
  },
})

const task3Formatting = createStep({
  id: 'task3: formatting',
  description: `Format the script exactly like this:`,
  inputSchema: z.object({Input_is_the_draft_script_produced_by: z.string()}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Format the script exactly like the specified template. Ensure each exchange is formatted as:
    // This step uses agent: formatter
    // const result = await formatter.generate('...')
    // TODO: Implement step logic
    throw new Error('task3: formatting not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * screenplay_creation_sequential
 *
 * Workflow pattern that sequentially runs analysis, scriptwriting, and formatting tasks, passing output to the next step.
 */
export const workflowPatternScreenplay = createWorkflow({
  id: 'screenplay_creation_sequential',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [task1Analysis, task2Scriptwriting, task3Formatting],
})
  .then(task1Analysis)
  .then(task2Scriptwriting)
  .then(task3Formatting)
  .commit()
