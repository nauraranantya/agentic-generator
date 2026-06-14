/**
 * Workflow: Streaming interaction workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * High-level workflow pattern capturing the user submission, agent streaming, tool call processing, UI updates, and text rendering as separate steps.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { agentFrontend } from '../agents/agentFrontend'

// Import tools used by workflow steps
import { toolAddPost } from '../tools/toolAddPost'

// ── Workflow Steps ──

const step01Start = createStep({
  id: 'Start: user submits message',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // User types text into the UI textarea and clicks Send; triggers setting isStreaming flag, clears previous responseText, and calls streamIt with prompt equal to the message.
    // This step uses agent: agentFrontend
    // const result = await agentFrontend.generate('...')
    // TODO: Implement step logic
    throw new Error('Start: user submits message not implemented yet')
  },
})

const step02StreamToAgent = createStep({
  id: 'Stream message to agent',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // The agent.stream call is invoked with { messages: prompt, clientTools: clientSideToolCallsMap }. This initiates a streaming response from the language model which may include tool call events and text parts.
    // This step uses agent: agentFrontend
    // const result = await agentFrontend.generate('...')
    // TODO: Implement step logic
    throw new Error('Stream message to agent not implemented yet')
  },
})

const step03ProcessStreamEvents = createStep({
  id: 'Process streaming events',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // The client processes the streaming response using response.processDataStream callbacks: onToolCallPart, onToolResultPart, onToolCallDeltaPart, onTextPart. onTextPart appends string parts to responseText. onToolCallPart executes matching client tool by name and args.
    // This step uses agent: agentFrontend
    // const result = await agentFrontend.generate('...')
    // TODO: Implement step logic
    throw new Error('Process streaming events not implemented yet')
  },
})

const step04HandleToolCalls = createStep({
  id: 'Handle tool calls and execute tools',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Tool call for 'addPost' triggers execute with args { color, name } and appends a post object to the posts array.
    // This step uses agent: agentFrontend
    // const result = await agentFrontend.generate('...')
    // This step uses tool: toolAddPost
    // TODO: Implement step logic
    throw new Error('Handle tool calls and execute tools not implemented yet')
  },
})

const step05AppendText = createStep({
  id: 'Append text parts to UI',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Each onTextPart callback appends the delivered text fragment to responseText. This task is repeated as streaming text parts arrive and results in updating the UI display region.
    // This step uses agent: agentFrontend
    // const result = await agentFrontend.generate('...')
    // TODO: Implement step logic
    throw new Error('Append text parts to UI not implemented yet')
  },
})

const step06End = createStep({
  id: 'End: streaming completed or cancelled',
  description: `Marks completion of the streaming interaction; 'isStreaming' flag in client is set to false on completion (note: runtime state not modeled in ontology).`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Marks completion of the streaming interaction; 'isStreaming' flag in client is set to false on completion (note: runtime state not modeled in ontology).
    // TODO: Implement step logic
    throw new Error('End: streaming completed or cancelled not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * Streaming interaction workflow
 *
 * High-level workflow pattern capturing the user submission, agent streaming, tool call processing, UI updates, and text rendering as separate steps.
 */
export const streamingWorkflow = createWorkflow({
  id: 'Streaming interaction workflow',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [step01Start, step02StreamToAgent, step03ProcessStreamEvents, step04HandleToolCalls, step05AppendText, step06End],
})
  .then(step01Start)
  .then(step02StreamToAgent)
  .then(step03ProcessStreamEvents)
  .then(step04HandleToolCalls)
  .then(step05AppendText)
  .then(step06End)
  .commit()
