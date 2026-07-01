/**
 * Workflow: workflow_image_crew
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { seniorPhotographerAgent, chiefCreativeDiretorAgent } from '../agents'

// ── Workflow Steps ──

const taskTakePhotograph = createStep({
  id: 'task_take_photograph',
  description: `Imagine and describe three photograph concepts for the Instagram post based on provided copy and product context.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // You MUST take the most amazing photo ever for an instagram post regarding the product. Provided ad copy: {copy}
    // This step uses agent: seniorPhotographerAgent
    // const result = await seniorPhotographerAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_take_photograph not implemented yet')
  },
})

const taskReviewPhoto = createStep({
  id: 'task_review_photo',
  description: `Review photography drafts, approve or request clarifications or delegations; ensure alignment with product goals.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Review the photos from the senior photographer. Ensure alignment with product goals; review, approve, ask clarifying questions or delegate follow-up work as necessary. When delegating, include the full draft as part of the information.
    // This step uses agent: chiefCreativeDiretorAgent
    // const result = await chiefCreativeDiretorAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_review_photo not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * workflow_image_crew
 */
export const workflowImageCrew = createWorkflow({
  id: 'workflow_image_crew',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [taskTakePhotograph, taskReviewPhoto],
})
  .then(taskTakePhotograph)
  .then(taskReviewPhoto)
  .commit()
