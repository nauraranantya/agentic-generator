/**
 * Workflow: yc_query_workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Semantic workflow: (1) Accept query input (natural language). (2) Agent decides to call yc-directory tool (if needed) to fetch or filter data. (3) Agent composes answer constrained to dataset fields and batch numbers only. (4) Optionally, evaluation runner can send agent responses to the relevancy scorer.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { ycDirectoryAgent } from '../agents'

// Import tools used by workflow steps
import { mastraEvalsRunner, ycDirectoryTool } from '../tools'

// ── Workflow Steps ──

const runEvalsTask = createStep({
  id: 'run_evals_task',
  description: `Task representing the tests/runEvals invocation that evaluates ycAgent using the AnswerRelevancyScorer with a small input dataset.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Task representing the tests/runEvals invocation that evaluates ycAgent using the AnswerRelevancyScorer with a small input dataset.
    // This step uses tool: mastraEvalsRunner
    // TODO: Implement step logic
    throw new Error('run_evals_task not implemented yet')
  },
})

const fetchYcDataTask = createStep({
  id: 'fetch_yc_data_task',
  description: `Task that represents the operation of the yc-directory tool's execute function returning YC data.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Task that represents the operation of the yc-directory tool's execute function returning YC data.
    // This step uses tool: ycDirectoryTool
    // TODO: Implement step logic
    throw new Error('fetch_yc_data_task not implemented yet')
  },
})

const answerYcDirectoryQuery = createStep({
  id: 'answer_yc_directory_query',
  description: `Primary task the ycDirectoryAgent performs: accept a natural language query about the YC 2024 directory and produce an answer exclusively using the yc-directory tool's dataset. Must include batch numbers when referencing companies and must not hallucinate beyond the available fields.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Primary task the ycDirectoryAgent performs: accept a natural language query about the YC 2024 directory and produce an answer exclusively using the yc-directory tool's dataset. Must include batch numbers when referencing companies and must not hallucinate beyond the available fields.
    // This step uses agent: ycDirectoryAgent
    // const result = await ycDirectoryAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('answer_yc_directory_query not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * yc_query_workflow
 *
 * Semantic workflow: (1) Accept query input (natural language). (2) Agent decides to call yc-directory tool (if needed) to fetch or filter data. (3) Agent composes answer constrained to dataset fields and batch numbers only. (4) Optionally, evaluation runner can send agent responses to the relevancy scorer.
 */
export const ycQueryWorkflow = createWorkflow({
  id: 'yc_query_workflow',
  inputSchema: z.object({Agent_decides_to_call_yc: z.string()}),
  outputSchema: z.object({}),
  steps: [runEvalsTask, fetchYcDataTask, answerYcDirectoryQuery],
})
  .parallel([runEvalsTask, fetchYcDataTask, answerYcDirectoryQuery])
  .commit()
