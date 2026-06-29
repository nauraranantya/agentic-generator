/**
 * Workflow: Chef Conversation Pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow demonstrating chefAgent usage: present ingredients, agent suggests recipe and high-level steps, demonstrate memory recall across threads/resources.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { chefAgent, memoryAgent } from '../agents'

// ── Workflow Steps ──

const taskInitialIngredientsQuery = createStep({
  id: 'Task: Initial Ingredients Query',
  description: `User asks: 'In my kitchen I have: pasta, canned tomatoes, garlic, olive oil, and some dried herbs (basil and oregano). What can I make? Please keep your answer brief, only give me the high level steps.' This is passed as input to chefAgent.stream with threadId and resourceId context.`,
  inputSchema: z.object({}),
  outputSchema: z.object({High: z.string()}),
  execute: async ({ inputData }) => {
    // In my kitchen I have: pasta, canned tomatoes, garlic, olive oil, and some dried herbs (basil and oregano). What can I make? Please keep your answer brief, only give me the high level steps.
    // This step uses agent: chefAgent
    // const result = await chefAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('Task: Initial Ingredients Query not implemented yet')
  },
})

const taskIngredientsAtFriendSHouse = createStep({
  id: 'Task: Ingredients at Friend's House',
  description: `User asks: 'Now I'm over at my friend's house, and they have: chicken thighs, coconut milk, sweet potatoes, and some curry powder.' This is passed to chefAgent.stream with same threadId/resourceId to append to conversation memory.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Now I'm over at my friend's house, and they have: chicken thighs, coconut milk, sweet potatoes, and some curry powder.
    // This step uses agent: chefAgent
    // const result = await chefAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('Task: Ingredients at Friend's House not implemented yet')
  },
})

const taskAskWhatWeCookedBefore = createStep({
  id: 'Task: Ask What We Cooked Before',
  description: `User asks: 'What did we cook before I went to my friends house?' This demonstrates memory recall options with memoryOptions: lastMessages=false and semanticRecall configured.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // What did we cook before I went to my friends house?
    // This step uses agent: chefAgent
    // const result = await chefAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('Task: Ask What We Cooked Before not implemented yet')
  },
})

const taskMemoryAgentRecallOperation = createStep({
  id: 'Task: Memory Agent Recall Operation',
  description: `Memory agent performs semantic recall according to configured memory options and may ask for user identification when missing.`,
  inputSchema: z.object({}),
  outputSchema: z.object({Start_or_re: z.string()}),
  execute: async ({ inputData }) => {
    // Chat with user started now <ISO_TIMESTAMP>. Don't mention this message. This means some time may have passed between this message and the one before. The user left and came back again. Say something to start the conversation up again. If there are no other messages besides this one then this is a new conversation.
    // This step uses agent: memoryAgent
    // const result = await memoryAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('Task: Memory Agent Recall Operation not implemented yet')
  },
})

const exit = createStep({
  id: 'Task: End / Exit',
  description: `Represents termination of the script after example interactions (process.exit in index.ts). Modeled as a conceptual task reflecting end of workflow.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Represents termination of the script after example interactions (process.exit in index.ts). Modeled as a conceptual task reflecting end of workflow.
    // This step uses agent: chefAgent
    // const result = await chefAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('Task: End / Exit not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * Chef Conversation Pattern
 *
 * Workflow demonstrating chefAgent usage: present ingredients, agent suggests recipe and high-level steps, demonstrate memory recall across threads/resources.
 */
export const chefConversationPattern = createWorkflow({
  id: 'Chef Conversation Pattern',
  inputSchema: z.object({Workflow_demonstrating_chefAgent_usage: z.string()}),
  outputSchema: z.object({}),
  steps: [taskInitialIngredientsQuery, taskIngredientsAtFriendSHouse, taskAskWhatWeCookedBefore, taskMemoryAgentRecallOperation, exit],
})
  .parallel([taskInitialIngredientsQuery, taskIngredientsAtFriendSHouse, taskAskWhatWeCookedBefore, taskMemoryAgentRecallOperation, exit])
  .commit()
