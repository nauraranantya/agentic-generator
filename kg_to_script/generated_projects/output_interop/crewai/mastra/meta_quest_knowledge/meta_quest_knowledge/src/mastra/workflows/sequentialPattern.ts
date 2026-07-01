/**
 * Workflow: sequential_pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { metaQuestExpert } from '../agents'

// ── Workflow Steps ──

const answerQuestionTask = createStep({
  id: 'answer_question_task',
  description: `Answer the user question with the most relevant information from the context and available knowledge sources.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Answer the user question with the most relevant information from the context and available knowledge sources.
    // This step uses agent: metaQuestExpert
    // const result = await metaQuestExpert.generate('...')
    // TODO: Implement step logic
    throw new Error('answer_question_task not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * sequential_pattern
 */
export const sequentialPattern = createWorkflow({
  id: 'sequential_pattern',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [answerQuestionTask],
})
  .parallel([answerQuestionTask])
  .commit()
