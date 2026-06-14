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
import { birdAgent } from '../agents/birdAgent'

// Import tools used by workflow steps
import { getRandomImageTool } from '../tools/getRandomImageTool'

// ── Workflow Steps ──

const stepStart = createStep({
  id: 'Start',
  description: `Initial step: user loads the UI or triggers a tag click (e.g., 'wildlife').`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Initial step: user loads the UI or triggers a tag click (e.g., 'wildlife').
    // TODO: Implement step logic
    throw new Error('Start not implemented yet')
  },
})

const stepGetImage = createStep({
  id: 'Get image',
  description: `Selects a tag value -> call tool to fetch a random image for that query.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Task to fetch a random image from Unsplash using a user-selected query option (wildlife, feathers, flying, birds).
    // This step uses tool: getRandomImageTool
    // TODO: Implement step logic
    throw new Error('Get image not implemented yet')
  },
})

const stepAnalyzeImage = createStep({
  id: 'Analyze image',
  description: `Sends the image and analysis prompt to the birdAgent; returns structured BirdResponse.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // view this image and let me know if it's a bird or not, and the scientific name of the bird without any explanation. Also summarize the location for this picture in one or two short sentences understandable by a high school student
    // This step uses agent: birdAgent
    // const result = await birdAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('Analyze image not implemented yet')
  },
})

const stepEnd = createStep({
  id: 'End',
  description: `Terminal step; UI displays results and attribution to the photographer.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Terminal step; UI displays results and attribution to the photographer.
    // TODO: Implement step logic
    throw new Error('End not implemented yet')
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
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [stepStart, stepGetImage, stepAnalyzeImage, stepEnd],
})
  .then(stepStart)
  .then(stepGetImage)
  .then(stepAnalyzeImage)
  .then(stepEnd)
  .commit()
