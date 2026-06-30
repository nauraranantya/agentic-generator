/**
 * Workflow: Workflow Pattern - Image Crew
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { seniorPhotographerAgent, chiefCreativeDirectorAgent } from '../agents'

// ── Workflow Steps ──

const taskTakePhotograph = createStep({
  id: 'task_take_photograph',
  description: `You are working on a new campaign for a super important customer,`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // (Full task prompt preserved)
    // This step uses agent: seniorPhotographerAgent
    // const result = await seniorPhotographerAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_take_photograph not implemented yet')
  },
})

const taskReviewPhoto = createStep({
  id: 'task_review_photo',
  description: `Review the photos you got from the senior photographer.`,
  inputSchema: z.object({}),
  outputSchema: z.object({Three_reviewed_photograph_descriptions_with_approval_and_optionally_delegated_follow: z.string()}),
  execute: async ({ inputData }) => {
    // (Full task prompt preserved)
    // This step uses agent: chiefCreativeDirectorAgent
    // const result = await chiefCreativeDirectorAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_review_photo not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * Workflow Pattern - Image Crew
 */
export const wpImageCrew = createWorkflow({
  id: 'Workflow Pattern - Image Crew',
  inputSchema: z.object({}),
  outputSchema: z.object({Three_reviewed_photograph_descriptions_with_approval_and_optionally_delegated_follow: z.string()}),
  steps: [taskTakePhotograph, taskReviewPhoto],
})
  .parallel([taskTakePhotograph, taskReviewPhoto])
  .commit()
