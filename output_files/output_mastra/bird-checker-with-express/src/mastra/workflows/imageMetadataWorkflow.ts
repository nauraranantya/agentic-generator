/**
 * Workflow: Image Metadata Workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * A simple two-step workflow: fetch a random image and analyze it for bird metadata. This workflow represents the server endpoints' functional logic.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { birdCheckerAgent } from '../agents/birdCheckerAgent'

// Import tools used by workflow steps
import { getRandomImageTool } from '../tools/getRandomImageTool'

// ── Workflow Steps ──

const stepFetchImage = createStep({
  id: 'Fetch Image Step',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Task that selects a random image from Unsplash using the getRandomImage tool with a query parameter drawn from an enum of options.
    // This step uses tool: getRandomImageTool
    // TODO: Implement step logic
    throw new Error('Fetch Image Step not implemented yet')
  },
})

const stepAnalyzeImage = createStep({
  id: 'Analyze Image Step',
  inputSchema: z.object({ type: z.any(), placeholder: z.any() }),
  outputSchema: z.object({ bird: z.boolean(), species: z.string(), location: z.string() }),
  execute: async ({ inputData }) => {
    // view this image and let me know if it's a bird or not, and the scientific name of the bird without any explanation. Also summarize the location for this picture in one or two short sentences understandable by a high school student
    // This step uses agent: birdCheckerAgent
    // const result = await birdCheckerAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('Analyze Image Step not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * Image Metadata Workflow
 *
 * A simple two-step workflow: fetch a random image and analyze it for bird metadata. This workflow represents the server endpoints' functional logic.
 */
export const imageMetadataWorkflow = createWorkflow({
  id: 'Image Metadata Workflow',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [stepFetchImage, stepAnalyzeImage],
})
  .then(stepFetchImage)
  .then(stepAnalyzeImage)
  .commit()
