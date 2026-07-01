/**
 * Workflow: Per-Resource Working Memory Pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { personalAssistant } from '../agents'

// ── Workflow Steps ──

const taskStartConversation = createStep({
  id: 'task_start_conversation',
  description: `Start a new conversation thread. System message template (in source):`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // New conversation thread started at {timestamp}. This may be a returning user - check your working memory to see if you know them already. If this is a new user, introduce yourself and learn about them. If this is a returning user, greet them warmly and reference what you remember!
    // This step uses agent: personalAssistant
    // const result = await personalAssistant.generate('...')
    // TODO: Implement step logic
    throw new Error('task_start_conversation not implemented yet')
  },
})

const taskUpdateMemory = createStep({
  id: 'task_update_memory',
  description: `Inspect conversation content and persist updates to per-resource working memory. Source code expects the agent to output updates wrapped with <working_memory> tags; updates are masked in the stream and persisted to LibSQL. UI uses a spinner during persistence but streaming semantics are an implementation detail (not modeled).`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // When you learn new facts about the user, produce updates wrapped in <working_memory> tags following the working memory template:
    // This step uses agent: personalAssistant
    // const result = await personalAssistant.generate('...')
    // TODO: Implement step logic
    throw new Error('task_update_memory not implemented yet')
  },
})

const taskInteractiveChat = createStep({
  id: 'task_interactive_chat',
  description: `Receive user messages, call the agent with memory context (resource + thread), stream responses to the user. The loop terminates when the user types 'exit' or 'quit'. The code obtains user input via Readline; runtime specifics are not modeled. The agent should use stored working memory where relevant.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // User input (pass-through). Behavior: if the input equals 'exit' or 'quit', end the session. Otherwise, send to agent with memory context { resource: <resource-id>, thread: <thread-id> }.
    // This step uses agent: personalAssistant
    // const result = await personalAssistant.generate('...')
    // TODO: Implement step logic
    throw new Error('task_interactive_chat not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * Per-Resource Working Memory Pattern
 */
export const perResourceWorkingMemoryPattern = createWorkflow({
  id: 'Per-Resource Working Memory Pattern',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [taskStartConversation, taskUpdateMemory, taskInteractiveChat],
})
  .then(taskStartConversation)
  .then(taskUpdateMemory)
  .then(taskInteractiveChat)
  .commit()
