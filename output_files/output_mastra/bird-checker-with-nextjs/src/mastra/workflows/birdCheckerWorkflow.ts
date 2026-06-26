/**
 * Workflow: Bird Checker workflow pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { birdChecker } from '../agents'

// Import tools used by workflow steps
import { getRandomImageTool } from '../tools'

// ── Workflow Steps ──

const fetchStep = createStep({
  id: 'Fetch random image task',
  description: `Get a random image from Unsplash using a selected query option`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Get a random image from Unsplash using a selected query option
    // This step uses tool: getRandomImageTool
    // TODO: Implement step logic
    throw new Error('Fetch random image task not implemented yet')
  },
})

const analyzeStep = createStep({
  id: 'Analyze image and produce bird metadata',
  description: `view this image and let me know if it's a bird or not, and the scientific name of the bird without any explanation. Also summarize the location for this picture in one or two short sentences understandable by a high school student`,
  inputSchema: z.object({image: z.string()}),
  outputSchema: z.object({bird: z.boolean()}),
  execute: async ({ inputData }) => {
    // view this image and let me know if it's a bird or not, and the scientific name of the bird without any explanation. Also summarize the location for this picture in one or two short sentences understandable by a high school student
    // This step uses agent: birdChecker
    // const result = await birdChecker.generate('...')
    // TODO: Implement step logic
    throw new Error('Analyze image and produce bird metadata not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * Bird Checker workflow pattern
 */
export const birdCheckerWorkflow = createWorkflow({
  id: 'Bird Checker workflow pattern',
  inputSchema: z.object({}),
  outputSchema: z.object({bird: z.boolean()}),
  steps: [fetchStep, analyzeStep],
})
  .then(fetchStep)
  .then(analyzeStep)
  .commit()
