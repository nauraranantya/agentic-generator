/**
 * Workflow: todo_chat_loop
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { todoAgent } from '../agents'

// ── Workflow Steps ──

const initReturnChatTask = createStep({
  id: 'init_return_chat_task',
  description: `Chat with user started now {timestamp}. Don't mention this message. This means some time has passed between this message and the one before. The user left and came back again. Say something to start the conversation up again.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Chat with user started now {timestamp}. Don't mention this message. This means some time has passed between this message and the one before. The user left and came back again. Say something to start the conversation up again.
    // This step uses agent: todoAgent
    // const result = await todoAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('init_return_chat_task not implemented yet')
  },
})

const presentListTask = createStep({
  id: 'present_list_task',
  description: `You are a helpful todolist AI agent. Help the user manage their todolist. If there is no list yet ask them what to add! If there is a list always print it out when the chat starts. For each item add emojis, dates, titles (with an index number starting at 1), descriptions, and statuses. For each piece of info add an emoji to the left of it. Also support subtask lists with bullet points inside a box. Help the user timebox each task by asking them how long it will take. You MUST save the todolist in every response message by printing out <working_memory> blocks. If you do not save it in working_memory you will forget - you only have access to one previous message at any time. The user is expecting you to save your memory in every interaction. If the user expresses any preference on how the list should be displayed, save that info in working_memory so you know how to format it later.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // You are a helpful todolist AI agent. Help the user manage their todolist. If there is no list yet ask them what to add! If there is a list always print it out when the chat starts. For each item add emojis, dates, titles (with an index number starting at 1), descriptions, and statuses. For each piece of info add an emoji to the left of it. Also support subtask lists with bullet points inside a box. Help the user timebox each task by asking them how long it will take. You MUST save the todolist in every response message by printing out <working_memory> blocks. If you do not save it in working_memory you will forget - you only have access to one previous message at any time. The user is expecting you to save your memory in every interaction. If the user expresses any preference on how the list should be displayed, save that info in working_memory so you know how to format it later.
    // This step uses agent: todoAgent
    // const result = await todoAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('present_list_task not implemented yet')
  },
})

const updateListTask = createStep({
  id: 'update_list_task',
  description: `You are a helpful todolist AI agent. Help the user manage their todolist. If there is no list yet ask them what to add! If there is a list always print it out when the chat starts. For each item add emojis, dates, titles (with an index number starting at 1), descriptions, and statuses. For each piece of info add an emoji to the left of it. Also support subtask lists with bullet points inside a box. Help the user timebox each task by asking them how long it will take. You MUST save the todolist in every response message by printing out <working_memory> blocks. If you do not save it in working_memory you will forget - you only have access to one previous message at any time. The user is expecting you to save your memory in every interaction. If the user expresses any preference on how the list should be displayed, save that info in working_memory so you know how to format it later.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // You are a helpful todolist AI agent. Help the user manage their todolist. If there is no list yet ask them what to add! If there is a list always print it out when the chat starts. For each item add emojis, dates, titles (with an index number starting at 1), descriptions, and statuses. For each piece of info add an emoji to the left of it. Also support subtask lists with bullet points inside a box. Help the user timebox each task by asking them how long it will take. You MUST save the todolist in every response message by printing out <working_memory> blocks. If you do not save it in working_memory you will forget - you only have access to one previous message at any time. The user is expecting you to save your memory in every interaction. If the user expresses any preference on how the list should be displayed, save that info in working_memory so you know how to format it later.
    // This step uses agent: todoAgent
    // const result = await todoAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('update_list_task not implemented yet')
  },
})

const timeboxTask = createStep({
  id: 'timebox_task',
  description: `You are a helpful todolist AI agent. Help the user manage their todolist. If there is no list yet ask them what to add! If there is a list always print it out when the chat starts. For each item add emojis, dates, titles (with an index number starting at 1), descriptions, and statuses. For each piece of info add an emoji to the left of it. Also support subtask lists with bullet points inside a box. Help the user timebox each task by asking them how long it will take. You MUST save the todolist in every response message by printing out <working_memory> blocks. If you do not save it in working_memory you will forget - you only have access to one previous message at any time. The user is expecting you to save your memory in every interaction. If the user expresses any preference on how the list should be displayed, save that info in working_memory so you know how to format it later.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // You are a helpful todolist AI agent. Help the user manage their todolist. If there is no list yet ask them what to add! If there is a list always print it out when the chat starts. For each item add emojis, dates, titles (with an index number starting at 1), descriptions, and statuses. For each piece of info add an emoji to the left of it. Also support subtask lists with bullet points inside a box. Help the user timebox each task by asking them how long it will take. You MUST save the todolist in every response message by printing out <working_memory> blocks. If you do not save it in working_memory you will forget - you only have access to one previous message at any time. The user is expecting you to save your memory in every interaction. If the user expresses any preference on how the list should be displayed, save that info in working_memory so you know how to format it later.
    // This step uses agent: todoAgent
    // const result = await todoAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('timebox_task not implemented yet')
  },
})

const saveWorkingMemoryTask = createStep({
  id: 'save_working_memory_task',
  description: `You MUST save the todolist in every response message by printing out <working_memory> blocks. If you do not save it in working_memory you will forget - you only have access to one previous message at any time. The user is expecting you to save your memory in every interaction. If the user expresses any preference on how the list should be displayed, save that info in working_memory so you know how to format it later.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // You MUST save the todolist in every response message by printing out <working_memory> blocks. If you do not save it in working_memory you will forget - you only have access to one previous message at any time. The user is expecting you to save your memory in every interaction. If the user expresses any preference on how the list should be displayed, save that info in working_memory so you know how to format it later.
    // This step uses agent: todoAgent
    // const result = await todoAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('save_working_memory_task not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * todo_chat_loop
 */
export const todoChatLoop = createWorkflow({
  id: 'todo_chat_loop',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [initReturnChatTask, presentListTask, updateListTask, timeboxTask, saveWorkingMemoryTask],
})
  .parallel([initReturnChatTask, presentListTask, updateListTask, timeboxTask, saveWorkingMemoryTask])
  .commit()
