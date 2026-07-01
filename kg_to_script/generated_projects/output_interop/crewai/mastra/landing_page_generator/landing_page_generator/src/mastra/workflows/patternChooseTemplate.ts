/**
 * Workflow: pattern_choose_template
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { seniorReactEngineer } from '../agents'

// ── Workflow Steps ──

const taskChooseTemplate = createStep({
  id: 'task_choose_template',
  description: `Learn the templates options choose and copy the one that suits the idea below the best, YOU MUST COPY, and then YOU MUST read the src/component in the directory you just copied, to decide what component files should be updated to make the landing page about the idea below.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Learn the templates options choose and copy the one that suits the idea below the best, YOU MUST COPY, and then YOU MUST read the src/component in the directory you just copied, to decide what component files should be updated to make the landing page about the idea below.
    // This step uses agent: seniorReactEngineer
    // const result = await seniorReactEngineer.generate('...')
    // TODO: Implement step logic
    throw new Error('task_choose_template not implemented yet')
  },
})

const taskUpdatePage = createStep({
  id: 'task_update_page',
  description: `READ the ./[chosen_template]/src/app/page.jsx OR ./[chosen_template]/src/app/(main)/page.jsx to learn its content and then write an updated version to the filesystem that removes any section related components that are not in our list from the returns. Keep the imports.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // READ the ./[chosen_template]/src/app/page.jsx OR ./[chosen_template]/src/app/(main)/page.jsx to learn its content and then write an updated version to the filesystem that removes any section related components that are not in our list from the returns. Keep the imports.
    // This step uses agent: seniorReactEngineer
    // const result = await seniorReactEngineer.generate('...')
    // TODO: Implement step logic
    throw new Error('task_update_page not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * pattern_choose_template
 */
export const patternChooseTemplate = createWorkflow({
  id: 'pattern_choose_template',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [taskChooseTemplate, taskUpdatePage],
})
  .then(taskChooseTemplate)
  .then(taskUpdatePage)
  .commit()
