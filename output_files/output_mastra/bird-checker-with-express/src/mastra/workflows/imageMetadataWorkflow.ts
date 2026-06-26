/**
 * Workflow: image_metadata_workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * A simple two-step workflow: fetch a random image and analyze it for bird metadata. This workflow represents the server endpoints' functional logic.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { birdChecker } from '../agents'

// Import tools used by workflow steps
import { getRandomImageTool } from '../tools'

// ── Workflow Steps ──

const stepFetchImage = createStep({
  id: 'step_fetch_image',
  description: `Task that selects a random image from Unsplash using the getRandomImage tool with a query parameter drawn from an enum of options.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Task that selects a random image from Unsplash using the getRandomImage tool with a query parameter drawn from an enum of options.
    // This step uses tool: getRandomImageTool
    // TODO: Implement step logic
    throw new Error('step_fetch_image not implemented yet')
  },
})

const stepAnalyzeImage = createStep({
  id: 'step_analyze_image',
  description: `Task that sends an image and an instruction prompt to the LLM agent to determine whether the image is a bird, the species (scientific name) and a short summary of the picture location.`,
  inputSchema: z.object({type: z.string(), placeholder: z.string()}),
  outputSchema: z.object({bird: z.string(), species: z.string(), location: z.string()}),
  execute: async ({ inputData }) => {
    // view this image and let me know if it's a bird or not, and the scientific name of the bird without any explanation. Also summarize the location for this picture in one or two short sentences understandable by a high school student
    // This step uses agent: birdChecker
    // const result = await birdChecker.generate('...')
    // TODO: Implement step logic
    throw new Error('step_analyze_image not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * image_metadata_workflow
 *
 * A simple two-step workflow: fetch a random image and analyze it for bird metadata. This workflow represents the server endpoints' functional logic.
 */
export const imageMetadataWorkflow = createWorkflow({
  id: 'image_metadata_workflow',
  inputSchema: z.object({A_simple_two_step_workflow: z.string()}),
  outputSchema: z.object({bird: z.string(), species: z.string(), location: z.string()}),
  steps: [stepFetchImage, stepAnalyzeImage],
})
  .then(stepFetchImage)
  .then(stepAnalyzeImage)
  .commit()
