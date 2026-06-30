/**
 * Workflow: stock_report_generation_pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Pattern created from the notebook 'L6-Planning_and_Stock_Report_Generation.ipynb'. Captures the sequence of roles (Admin/Planner/Engineer/Executor/Writer), their responsibilities, and the artifacts exchanged.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { plannerAgent, engineerAgent, executorAgent, writerAgent } from '../agents'

// Import tools used by workflow steps
import { codingEnvironmentTool } from '../tools'

// ── Workflow Steps ──

const mainTask = createStep({
  id: 'main_task',
  description: `Top-level task given by Admin that initiates the workflow. Text preserved in MainTaskPrompt.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Write a blogpost about the stock price performance of Nvidia in the past month. Today's date is 2024-04-23.
    // TODO: Implement step logic
    throw new Error('main_task not implemented yet')
  },
})

const planInformationTask = createStep({
  id: 'plan_information_task',
  description: `Planner determines which information (stock prices, date range, sources, computation methods) is needed and specifies steps for retrieving it using Python code.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Given a task, please determine what information is needed to complete the task. Please note that the information will all be retrieved using Python code. Please only suggest information that can be retrieved using Python code. After each step is done by others, check the progress and instruct the remaining steps. If a step fails, try to workaround
    // This step uses agent: plannerAgent
    // const result = await plannerAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('plan_information_task not implemented yet')
  },
})

const writeCodeTask = createStep({
  id: 'write_code_task',
  description: `Engineer implements Python code to retrieve stock data, compute required metrics, and produce artifacts for the writer. Code artifact contains instructions like 'retrieve historic prices, compute performance over last month, format data for report'.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // An engineer that writes code based on the plan provided by the planner.
    // This step uses agent: engineerAgent
    // const result = await engineerAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('write_code_task not implemented yet')
  },
})

const executeCodeTask = createStep({
  id: 'execute_code_task',
  description: `Executor runs the code produced by the Engineer in a specified working directory and returns execution outputs (e.g., numerical results, csv, figures). Execution config preserved on ExecutorConfig_Execution.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Execute the code written by the engineer and report the result.
    // This step uses agent: executorAgent
    // const result = await executorAgent.generate('...')
    // This step uses tool: codingEnvironmentTool
    // TODO: Implement step logic
    throw new Error('execute_code_task not implemented yet')
  },
})

const writeReportTask = createStep({
  id: 'write_report_task',
  description: `Writer composes the blog post using execution results; writes in markdown format with relevant titles and places content inside a pseudo \`\`\`md\`\`\` code block. The writer should accept feedback from Admin and refine the blog.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Writer.
    // This step uses agent: writerAgent
    // const result = await writerAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('write_report_task not implemented yet')
  },
})

const adminFeedbackTask = createStep({
  id: 'admin_feedback_task',
  description: `Admin (user_proxy) reviews the blog draft and provides feedback; the Writer will refine the blog accordingly. Modeled as a Task performed by a HumanAgent.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Admin (user_proxy) reviews the blog draft and provides feedback; the Writer will refine the blog accordingly. Modeled as a Task performed by a HumanAgent.
    // TODO: Implement step logic
    throw new Error('admin_feedback_task not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * stock_report_generation_pattern
 *
 * Pattern created from the notebook 'L6-Planning_and_Stock_Report_Generation.ipynb'. Captures the sequence of roles (Admin/Planner/Engineer/Executor/Writer), their responsibilities, and the artifacts exchanged.
 */
export const stockReportGenerationPattern = createWorkflow({
  id: 'stock_report_generation_pattern',
  inputSchema: z.object({L6: z.string()}),
  outputSchema: z.object({}),
  steps: [mainTask, planInformationTask, writeCodeTask, executeCodeTask, writeReportTask, adminFeedbackTask],
})
  .parallel([mainTask, planInformationTask, writeCodeTask, executeCodeTask, writeReportTask, adminFeedbackTask])
  .commit()
