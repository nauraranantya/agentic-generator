/**
 * Workflow: Mastra conversational flow (example run)
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { memoryAgent, chefAgent } from '../agents'

// ── Workflow Steps ──

const setUpSessionAndThread = createStep({
  id: 'Set up session and thread',
  description: `Represents creating a thread/session id for streaming interactions. In source a randomUUID() is used for threadId; resourceId is set to 'SOME_USER_ID'.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Represents creating a thread/session id for streaming interactions. In source a randomUUID() is used for threadId; resourceId is set to 'SOME_USER_ID'.
    // This step uses agent: memoryAgent
    // const result = await memoryAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('Set up session and thread not implemented yet')
  },
})

const suggestRecipesFromUserSListedIngredients = createStep({
  id: 'Suggest recipes from user's listed ingredients',
  description: `User asks the agent: 'In my kitchen I have: pasta, canned tomatoes, garlic, olive oil, and some dried herbs (basil and oregano). What can I make? Please keep your answer brief, only give me the high level steps.' This exact string is captured in Prompt_InitialIngredients and used as input to the ChefAgent.`,
  inputSchema: z.object({}),
  outputSchema: z.object({high: z.string()}),
  execute: async ({ inputData }) => {
    // In my kitchen I have: pasta, canned tomatoes, garlic, olive oil, and some dried herbs (basil and oregano). What can I make? Please keep your answer brief, only give me the high level steps.
    // This step uses agent: chefAgent
    // const result = await chefAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('Suggest recipes from user's listed ingredients not implemented yet')
  },
})

const suggestRecipesFromFriendSIngredients = createStep({
  id: 'Suggest recipes from friend's ingredients',
  description: `User asks: 'Now I'm over at my friend's house, and they have: chicken thighs, coconut milk, sweet potatoes, and some curry powder.' Captured exactly in Prompt_FriendIngredients.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Now I'm over at my friend's house, and they have: chicken thighs, coconut milk, sweet potatoes, and some curry powder.
    // This step uses agent: chefAgent
    // const result = await chefAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('Suggest recipes from friend's ingredients not implemented yet')
  },
})

const recallWhatWasCookedPreviously = createStep({
  id: 'Recall what was cooked previously',
  description: `User asks: 'What did we cook before I went to my friends house?' In source, this call is made with memoryOptions: { lastMessages: 3 } to override recall settings for that call. That override is captured in Task_MemoryOverride_Config.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // What did we cook before I went to my friends house?
    // This step uses agent: chefAgent
    // const result = await chefAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('Recall what was cooked previously not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * Mastra conversational flow (example run)
 */
export const mastraConversationPattern = createWorkflow({
  id: 'Mastra conversational flow (example run)',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [setUpSessionAndThread, suggestRecipesFromUserSListedIngredients, suggestRecipesFromFriendSIngredients, recallWhatWasCookedPreviously],
})
  .parallel([setUpSessionAndThread, suggestRecipesFromUserSListedIngredients, suggestRecipesFromFriendSIngredients, recallWhatWasCookedPreviously])
  .commit()
