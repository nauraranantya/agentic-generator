/**
 * Workflow: Bird Checker Workflow Pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * High-level workflow: Start -> Get Image -> Analyze Image -> End. Describes how UI tags trigger image fetch and analysis by the agent.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { birdAgent } from '../agents'

// Import tools used by workflow steps
import { getRandomImageTool } from '../tools'

// ── Workflow Steps ──

const getRandomImageTask = createStep({
  id: 'Get Random Image Task',
  description: `Task to fetch a random image from Unsplash using a user-selected query option (wildlife, feathers, flying, birds).`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Task to fetch a random image from Unsplash using a user-selected query option (wildlife, feathers, flying, birds).
    // This step uses tool: getRandomImageTool
    // TODO: Implement step logic
    throw new Error('Get Random Image Task not implemented yet')
  },
})

const analyzeImageTask = createStep({
  id: 'Analyze Image Task',
  description: `Task to analyze an image and determine whether it is a bird, the species scientific name, and a short location summary. Implemented via the birdAgent (agent.generate with an image and a text instruction).`,
  inputSchema: z.object({}),
  outputSchema: z.object({ bird: z.boolean(), species: z.string(), location: z.string() }),
  execute: async ({ inputData }) => {
    // view this image and let me know if it's a bird or not, and the scientific name of the bird without any explanation. Also summarize the location for this picture in one or two short sentences understandable by a high school student
    // This step uses agent: birdAgent
    // const result = await birdAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('Analyze Image Task not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * Bird Checker Workflow Pattern
 *
 * High-level workflow: Start -> Get Image -> Analyze Image -> End. Describes how UI tags trigger image fetch and analysis by the agent.
 */
export const birdCheckerWorkflow = createWorkflow({
  id: 'Bird Checker Workflow Pattern',
  inputSchema: z.object({High_level_workflow: z.string()}),
  outputSchema: z.object({ bird: z.boolean(), species: z.string(), location: z.string() }),
  steps: [getRandomImageTask, analyzeImageTask],
})
  .then(getRandomImageTask)
  .then(analyzeImageTask)
  .commit()
