/**
 * Workflow: conversation_with_memory_pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Pattern in chat.ts showing a memory-aware conversation: system re-engagement message, interactive user loop, and memory-backed recall/persistence.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { memoryAgent } from '../agents'

// ── Workflow Steps ──

const taskChatStartConversation = createStep({
  id: 'task_chat_start_conversation',
  description: `On startup a system message (Prompt_Chat_SystemStart) is sent to the memory agent. This is used to re-engage a returning user and may include a dynamic timestamp.`,
  inputSchema: z.object({Note: z.string()}),
  outputSchema: z.object({A_short_re: z.string()}),
  execute: async ({ inputData }) => {
    // Chat with user started now \${ISO_TIMESTAMP}. Don't mention this message. This means some time may have passed between this message and the one before. The user left and came back again. Say something to start the conversation up again.
    // This step uses agent: memoryAgent
    // const result = await memoryAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_chat_start_conversation not implemented yet')
  },
})

const taskChatInteractiveMessage = createStep({
  id: 'task_chat_interactive_message',
  description: `Loop of receiving a user message and calling memoryAgent.stream(prompt, { memory: { thread, resource } }). The user message is forwarded as Prompt_Chat_UserMessage_Template at runtime with concrete content.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // User message (free text). In the interactive loop the contents are forwarded directly to the memoryAgent.
    // This step uses agent: memoryAgent
    // const result = await memoryAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_chat_interactive_message not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * conversation_with_memory_pattern
 *
 * Pattern in chat.ts showing a memory-aware conversation: system re-engagement message, interactive user loop, and memory-backed recall/persistence.
 */
export const conversationWithMemoryPattern = createWorkflow({
  id: 'conversation_with_memory_pattern',
  inputSchema: z.object({ts_showing_a_memory_aware_conversation: z.string()}),
  outputSchema: z.object({}),
  steps: [taskChatStartConversation, taskChatInteractiveMessage],
})
  .then(taskChatStartConversation)
  .then(taskChatInteractiveMessage)
  .commit()
