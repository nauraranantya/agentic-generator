/**
 * Workflow: YC directory query workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Semantic workflow: (1) Accept query input (natural language). (2) Agent decides to call yc-directory tool (if needed) to fetch or filter data. (3) Agent composes answer constrained to dataset fields and batch numbers only. (4) Optionally, evaluation runner can send agent responses to the relevancy scorer.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { ycDirectoryAgent } from '../agents/ycDirectoryAgent'

// Import tools used by workflow steps
import { mastraEvalsRunner } from '../tools/mastraEvalsRunner'
import { ycDirectoryTool } from '../tools/ycDirectoryTool'

// ── Workflow Steps ──

const stepAcceptQuery = createStep({
  id: 'Accept query input',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Task representing the tests/runEvals invocation that evaluates ycAgent using the AnswerRelevancyScorer with a small input dataset.
    // This step uses tool: mastraEvalsRunner
    // TODO: Implement step logic
    throw new Error('Accept query input not implemented yet')
  },
})

const stepCallTool = createStep({
  id: 'Call yc-directory tool to fetch/filter data',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Task that represents the operation of the yc-directory tool's execute function returning YC data.
    // This step uses tool: ycDirectoryTool
    // TODO: Implement step logic
    throw new Error('Call yc-directory tool to fetch/filter data not implemented yet')
  },
})

const stepGenerateAnswer = createStep({
  id: 'Generate constrained answer',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Primary task the ycDirectoryAgent performs: accept a natural language query about the YC 2024 directory and produce an answer exclusively using the yc-directory tool's dataset. Must include batch numbers when referencing companies and must not hallucinate beyond the available fields.
    // This step uses agent: ycDirectoryAgent
    // const result = await ycDirectoryAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('Generate constrained answer not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * YC directory query workflow
 *
 * Semantic workflow: (1) Accept query input (natural language). (2) Agent decides to call yc-directory tool (if needed) to fetch or filter data. (3) Agent composes answer constrained to dataset fields and batch numbers only. (4) Optionally, evaluation runner can send agent responses to the relevancy scorer.
 */
export const ycQueryWorkflow = createWorkflow({
  id: 'YC directory query workflow',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [stepAcceptQuery, stepCallTool, stepGenerateAnswer],
})
  // NOTE: Branching workflow — simplified to sequential for type compatibility
  // TODO: Implement conditional branching using .branch() API
  .then(stepAcceptQuery)
  .then(stepCallTool)
  .then(stepGenerateAnswer)
  .commit()
