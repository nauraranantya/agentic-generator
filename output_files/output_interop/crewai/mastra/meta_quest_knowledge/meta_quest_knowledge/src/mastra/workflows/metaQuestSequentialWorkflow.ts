/**
 * Workflow: meta_quest_sequential_workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * A sequential workflow: start -> answer question -> end. Process type: sequential (Process.sequential in source code).
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { metaQuestExpert } from '../agents'

// ── Workflow Steps ──

const answerQuestionTask = createStep({
  id: 'answer_question_task',
  description: `Answer the user question with the most relevant information from the context and available knowledge sources. Question: {question}`,
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
 * meta_quest_sequential_workflow
 *
 * A sequential workflow: start -> answer question -> end. Process type: sequential (Process.sequential in source code).
 */
export const metaQuestSequentialWorkflow = createWorkflow({
  id: 'meta_quest_sequential_workflow',
  inputSchema: z.object({A_sequential_workflow: z.string()}),
  outputSchema: z.object({}),
  steps: [answerQuestionTask],
})
  .then(answerQuestionTask)
  .commit()
