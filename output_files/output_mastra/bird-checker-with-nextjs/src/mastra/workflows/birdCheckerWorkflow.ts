/**
 * Workflow: Bird Checker workflow pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { birdAgent } from '../agents/birdAgent'

// Import tools used by workflow steps
import { getRandomImageTool } from '../tools/getRandomImageTool'

// ── Workflow Steps ──

const fetchStep = createStep({
  id: 'Fetch image step',
  inputSchema: z.object({ query: z.any() }),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Get a random image from Unsplash using a selected query option
    // This step uses tool: getRandomImageTool
    // TODO: Implement step logic
    throw new Error('Fetch image step not implemented yet')
  },
})

const analyzeStep = createStep({
  id: 'Analyze image step',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // view this image and let me know if it's a bird or not, and the scientific name of the bird without any explanation. Also summarize the location for this picture in one or two short sentences understandable by a high school student
    // This step uses agent: birdAgent
    // const result = await birdAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('Analyze image step not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * Bird Checker workflow pattern
 */
export const birdCheckerWorkflow = createWorkflow({
  id: 'Bird Checker workflow pattern',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [fetchStep, analyzeStep],
})
  .then(fetchStep)
  .then(analyzeStep)
  .commit()
