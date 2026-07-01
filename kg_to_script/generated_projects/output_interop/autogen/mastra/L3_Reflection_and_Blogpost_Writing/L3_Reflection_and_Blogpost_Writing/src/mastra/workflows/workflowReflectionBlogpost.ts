/**
 * Workflow: Reflection and Blogpost Writing Workflow Pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow that generates a blogpost draft, then uses a critic and nested reviewers (SEO, Legal, Ethics) with a meta reviewer to aggregate suggestions and refine the draft.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { writer1, ethicsReviewer1, metaReviewer1 } from '../agents'

// ── Workflow Steps ──

const blogpostGenerationTask = createStep({
  id: 'Blogpost generation task',
  description: `Task instructs the Writer to produce a concise but engaging blogpost about DeepLearning.AI within 100 words.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Write a concise but engaging blogpost about
    // This step uses agent: writer1
    // const result = await writer1.generate('...')
    // TODO: Implement step logic
    throw new Error('Blogpost generation task not implemented yet')
  },
})

const ethicsReviewTask = createStep({
  id: 'Ethics review task',
  description: `Review the following content. Return review into as JSON object only: {'reviewer': '', 'review': ''}.`,
  inputSchema: z.object({}),
  outputSchema: z.object({Fields: z.string()}),
  execute: async ({ inputData }) => {
    // Review the following content. Return review into as JSON object only: {'reviewer': '', 'review': ''}.
    // This step uses agent: ethicsReviewer1
    // const result = await ethicsReviewer1.generate('...')
    // TODO: Implement step logic
    throw new Error('Ethics review task not implemented yet')
  },
})

const metaAggregationTask = createStep({
  id: 'Meta aggregation task',
  description: `This task consumes JSON outputs from SEO, Legal, and Ethics reviewers and produces a consolidated suggestion object (the notebook orchestrates this via the Critic.register_nested_chats and nested chat flow).`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Aggregate feedback from all reviewers and give final suggestions on the writing.
    // This step uses agent: metaReviewer1
    // const result = await metaReviewer1.generate('...')
    // TODO: Implement step logic
    throw new Error('Meta aggregation task not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * Reflection and Blogpost Writing Workflow Pattern
 *
 * Workflow that generates a blogpost draft, then uses a critic and nested reviewers (SEO, Legal, Ethics) with a meta reviewer to aggregate suggestions and refine the draft.
 */
export const workflowReflectionBlogpost = createWorkflow({
  id: 'Reflection and Blogpost Writing Workflow Pattern',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [blogpostGenerationTask, ethicsReviewTask, metaAggregationTask],
})
  .then(blogpostGenerationTask)
  .then(ethicsReviewTask)
  .then(metaAggregationTask)
  .commit()
