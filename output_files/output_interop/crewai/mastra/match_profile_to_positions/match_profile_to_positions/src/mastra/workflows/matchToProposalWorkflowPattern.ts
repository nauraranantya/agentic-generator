/**
 * Workflow: match_to_proposal_workflow_pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Sequential workflow: 1) read CV -> 2) match CV to jobs
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { cvReader, matcher } from '../agents'

// ── Workflow Steps ──

const readCvTask = createStep({
  id: 'read_cv_task',
  description: `Task: extract structured summary from input CV file.`,
  inputSchema: z.object({path_to_cv: z.string()}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Extract relevant information from the given CV. Focus on skills, experience,
    // This step uses agent: cvReader
    // const result = await cvReader.generate('...')
    // TODO: Implement step logic
    throw new Error('read_cv_task not implemented yet')
  },
})

const matchCvTask = createStep({
  id: 'match_cv_task',
  description: `Task: match structured CV summary against job opportunities CSV and produce ranked list.`,
  inputSchema: z.object({path_to_jobs_csv: z.string(), path_to_cv: z.string()}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Match the CV to the job opportunities based on skills, experience, and key
    // This step uses agent: matcher
    // const result = await matcher.generate('...')
    // TODO: Implement step logic
    throw new Error('match_cv_task not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * match_to_proposal_workflow_pattern
 *
 * Sequential workflow: 1) read CV -> 2) match CV to jobs
 */
export const matchToProposalWorkflowPattern = createWorkflow({
  id: 'match_to_proposal_workflow_pattern',
  inputSchema: z.object({path_to_cv: z.string()}),
  outputSchema: z.object({}),
  steps: [readCvTask, matchCvTask],
})
  .then(readCvTask)
  .then(matchCvTask)
  .commit()
