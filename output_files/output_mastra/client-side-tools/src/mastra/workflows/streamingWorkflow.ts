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
import { agent } from '../agents'

// Import tools used by workflow steps
import { toolAddPost } from '../tools'

// ── Workflow Steps ──

const userSubmitsMessage = createStep({
  id: 'User submits message',
  description: `User types text into the UI textarea and clicks Send; triggers setting isStreaming flag, clears previous responseText, and calls streamIt with prompt equal to the message.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // User types text into the UI textarea and clicks Send; triggers setting isStreaming flag, clears previous responseText, and calls streamIt with prompt equal to the message.
    // This step uses agent: agent
    // const result = await agent.generate('...')
    // TODO: Implement step logic
    throw new Error('User submits message not implemented yet')
  },
})

const streamMessageToAgent = createStep({
  id: 'Stream message to agent',
  description: `The agent.stream call is invoked with { messages: prompt, clientTools: clientSideToolCallsMap }. This initiates a streaming response from the language model which may include tool call events and text parts.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // The agent.stream call is invoked with { messages: prompt, clientTools: clientSideToolCallsMap }. This initiates a streaming response from the language model which may include tool call events and text parts.
    // This step uses agent: agent
    // const result = await agent.generate('...')
    // TODO: Implement step logic
    throw new Error('Stream message to agent not implemented yet')
  },
})

const processStreamedEventsToolCallsToolResultsDeltasTextParts = createStep({
  id: 'Process streamed events (tool calls, tool results, deltas, text parts)',
  description: `The client processes the streaming response using response.processDataStream callbacks: onToolCallPart, onToolResultPart, onToolCallDeltaPart, onTextPart. onTextPart appends string parts to responseText. onToolCallPart executes matching client tool by name and args.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // The client processes the streaming response using response.processDataStream callbacks: onToolCallPart, onToolResultPart, onToolCallDeltaPart, onTextPart. onTextPart appends string parts to responseText. onToolCallPart executes matching client tool by name and args.
    // This step uses agent: agent
    // const result = await agent.generate('...')
    // TODO: Implement step logic
    throw new Error('Process streamed events (tool calls, tool results, deltas, text parts) not implemented yet')
  },
})

const executeAddPostTool = createStep({
  id: 'Execute addPost tool',
  description: `Tool call for 'addPost' triggers execute with args { color, name } and appends a post object to the posts array.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Tool call for 'addPost' triggers execute with args { color, name } and appends a post object to the posts array.
    // This step uses agent: agent
    // const result = await agent.generate('...')
    // This step uses tool: toolAddPost
    // TODO: Implement step logic
    throw new Error('Execute addPost tool not implemented yet')
  },
})

const appendTextPartsToTheResponseTextState = createStep({
  id: 'Append text parts to the responseText state',
  description: `Each onTextPart callback appends the delivered text fragment to responseText. This task is repeated as streaming text parts arrive and results in updating the UI display region.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Each onTextPart callback appends the delivered text fragment to responseText. This task is repeated as streaming text parts arrive and results in updating the UI display region.
    // This step uses agent: agent
    // const result = await agent.generate('...')
    // TODO: Implement step logic
    throw new Error('Append text parts to the responseText state not implemented yet')
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
  inputSchema: z.object({High: z.string()}),
  outputSchema: z.object({}),
  steps: [userSubmitsMessage, streamMessageToAgent, processStreamedEventsToolCallsToolResultsDeltasTextParts, executeAddPostTool, appendTextPartsToTheResponseTextState],
})
  .then(userSubmitsMessage)
  .then(streamMessageToAgent)
  .then(processStreamedEventsToolCallsToolResultsDeltasTextParts)
  .then(executeAddPostTool)
  .then(appendTextPartsToTheResponseTextState)
  .commit()
