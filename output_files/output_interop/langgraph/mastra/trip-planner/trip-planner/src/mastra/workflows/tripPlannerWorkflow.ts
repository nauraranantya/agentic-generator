/**
 * Workflow: trip_planner_workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * An agent workflow (StateGraph) named "Trip Planner". It contains three primary workflow steps (classify, extraction, callTools) with conditional branching:
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { tripPlannerAgent } from '../agents'

// ── Workflow Steps ──

const taskExtraction = createStep({
  id: 'task_extraction',
  description: `Extraction task: given the entire conversation history, call a tool named "extract" with the following schema:`,
  inputSchema: z.object({}),
  outputSchema: z.object({JSON: z.string()}),
  execute: async ({ inputData }) => {
    // You're an AI assistant for planning trips. The user has requested information about a trip they want to go on.
    // This step uses agent: tripPlannerAgent
    // const result = await tripPlannerAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_extraction not implemented yet')
  },
})

const taskClassify = createStep({
  id: 'task_classify',
  description: `Classification task: use a tool named "classify" with schema { isRelevant: boolean } to determine if previously extracted tripDetails remain relevant to the user's most recent message.`,
  inputSchema: z.object({}),
  outputSchema: z.object({isRelevant: z.boolean()}),
  execute: async ({ inputData }) => {
    // You're an AI assistant for planning trips. The user has already specified the following details for their trip:
    // This step uses agent: tripPlannerAgent
    // const result = await tripPlannerAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_classify not implemented yet')
  },
})

const taskCallTools = createStep({
  id: 'task_call_tools',
  description: `CallTools task: binds ACCOMMODATIONS_TOOLS (list-accommodations and list-restaurants), invokes the language model to decide which tool(s) to call, and pushes UI items for results. The LLM receives the system message:`,
  inputSchema: z.object({}),
  outputSchema: z.object({list: z.string()}),
  execute: async ({ inputData }) => {
    // You are an AI assistant who helps users book trips. Use the user's most recent message(s) to contextually generate a response.
    // This step uses agent: tripPlannerAgent
    // const result = await tripPlannerAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_call_tools not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * trip_planner_workflow
 *
 * An agent workflow (StateGraph) named "Trip Planner". It contains three primary workflow steps (classify, extraction, callTools) with conditional branching:
 */
export const tripPlannerWorkflow = createWorkflow({
  id: 'trip_planner_workflow',
  inputSchema: z.object({At_START: z.string()}),
  outputSchema: z.object({list: z.string()}),
  steps: [taskExtraction, taskClassify, taskCallTools],
})
  // NOTE: Branching workflow — simplified to sequential for type compatibility
  // TODO: Implement conditional branching using .branch() API
  .then(taskExtraction)
  .then(taskClassify)
  .then(taskCallTools)
  .commit()
