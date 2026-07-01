/**
 * Workflow: writer_workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow representing the StateGraph: START -> prepare -> writer -> suggestions.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { writerAnnotationAgentUuid1 } from '../agents'

// ── Workflow Steps ──

const prepareTask = createStep({
  id: 'prepare_task',
  description: `Binds the tool 'draft_text_document' with the model and streams its output (initStream). If state.context.writer.selected is present, a system message of 'Selected text in question: <selected>' is prepended. As model stream chunks arrive, tool call arguments (title, description) are extracted and a UI 'writer' component is populated with these arguments and isGenerating=true. Produces a draft candidate resource representing the tool call output.`,
  inputSchema: z.object({State: z.string()}),
  outputSchema: z.object({title: z.string()}),
  execute: async ({ inputData }) => {
    // (used as tool description binding to model) Prepare a text document for the user with a short title and short description for browsing purposes. Can be also used when creating a new version of the document.
    // This step uses agent: writerAnnotationAgentUuid1
    // const result = await writerAnnotationAgentUuid1.generate('...')
    // TODO: Implement step logic
    throw new Error('prepare_task not implemented yet')
  },
})

const writeTask = createStep({
  id: 'write_task',
  description: `Generates the final text document content. Uses a non-streaming model invocation (tags ['nostream']) in implementation to get full content; however the code also uses a streaming invocation to update UI content progressively. System instruction: 'Write a text document based on the user's request. Only output the content, do not ask any additional questions.' If state.context.writer.selected is present the selected text is appended to the system instruction. Consumes conversation history and tool outputs; produces the final document content resource (FinalTextDocument).`,
  inputSchema: z.object({excluding_the_last_tool: z.string()}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Write a text document based on the user's request. Only output the content, do not ask any additional questions.
    // This step uses agent: writerAnnotationAgentUuid1
    // const result = await writerAnnotationAgentUuid1.generate('...')
    // TODO: Implement step logic
    throw new Error('write_task not implemented yet')
  },
})

const suggestionsTask = createStep({
  id: 'suggestions_task',
  description: `Takes the last AI message; for each tool call in the message, emits a tool-type message 'Finished' referencing the tool_call id. Then invokes the model with the updated messages and appends the model's finish message to the conversation. This step does non-streaming invocation in the implementation (model.invoke).`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Process the last AI message tool_calls: for each tool call, add a tool message 'Finished' referencing the call id, then invoke the model with the updated messages to produce a finishing message.
    // This step uses agent: writerAnnotationAgentUuid1
    // const result = await writerAnnotationAgentUuid1.generate('...')
    // TODO: Implement step logic
    throw new Error('suggestions_task not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * writer_workflow
 *
 * Workflow representing the StateGraph: START -> prepare -> writer -> suggestions.
 */
export const writerWorkflow = createWorkflow({
  id: 'writer_workflow',
  inputSchema: z.object({Workflow_representing_the_StateGraph: z.string()}),
  outputSchema: z.object({}),
  steps: [prepareTask, writeTask, suggestionsTask],
})
  .parallel([prepareTask, writeTask, suggestionsTask])
  .commit()
