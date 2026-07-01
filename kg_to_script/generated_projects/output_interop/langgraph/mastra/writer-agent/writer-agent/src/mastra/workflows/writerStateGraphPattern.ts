/**
 * Workflow: writer_state_graph_pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { writerAgent } from '../agents'

// ── Workflow Steps ──

const taskPrepare = createStep({
  id: 'task_prepare',
  description: `Create an initial draft of the document by invoking the bound tool and streaming response to the UI.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Prepare a text document for the user with a short title and short description for browsing purposes. Can be also used when creating a new version of the document.
    // This step uses agent: writerAgent
    // const result = await writerAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_prepare not implemented yet')
  },
})

const taskWriter = createStep({
  id: 'task_writer',
  description: `Generate the full document content based on the user's request and earlier messages; stream to UI, then finalise.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Write a text document based on the user's request. Only output the content, do not ask any additional questions. If there is selected text in state.context.writer.selected, include that context in the generation.
    // This step uses agent: writerAgent
    // const result = await writerAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_writer not implemented yet')
  },
})

const taskSuggestions = createStep({
  id: 'task_suggestions',
  description: `Call the model to produce a finishing/suggestions message based on collected messages and tool call completions.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Invoke the model on the conversation messages (including tool finished signals) to produce the finish/suggestions message; append the resulting model output to the message stream.
    // This step uses agent: writerAgent
    // const result = await writerAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_suggestions not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * writer_state_graph_pattern
 */
export const writerStateGraphPattern = createWorkflow({
  id: 'writer_state_graph_pattern',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [taskPrepare, taskWriter, taskSuggestions],
})
  .then(taskPrepare)
  .then(taskWriter)
  .then(taskSuggestions)
  .commit()
