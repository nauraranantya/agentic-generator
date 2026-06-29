/**
 * Workflow: recipe_workflow_pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Sequence in index.ts showing Chef Agent receiving ingredients, producing suggestions, and recalling prior suggestions using shared memory.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { chefAgent } from '../agents'

// ── Workflow Steps ──

const taskRecipeSuggestInitialQuery = createStep({
  id: 'task_recipe_suggest_initial_query',
  description: `Agent.stream called with Prompt_Index_WhatCanIMake; ChefAgent produces short high-level steps. The call includes threadId and resourceId parameters to enable memory association.`,
  inputSchema: z.object({}),
  outputSchema: z.object({A_short_list_of_possible_recipes_with_high: z.string()}),
  execute: async ({ inputData }) => {
    // In my kitchen I have: pasta, canned tomatoes, garlic, olive oil, and some dried herbs (basil and oregano). What can I make? Please keep your answer brief, only give me the high level steps.
    // This step uses agent: chefAgent
    // const result = await chefAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_recipe_suggest_initial_query not implemented yet')
  },
})

const taskRecipeSuggestFriendsHouseQuery = createStep({
  id: 'task_recipe_suggest_friends_house_query',
  description: `Agent.stream called with Prompt_Index_FriendsHouse to produce alternative recipes. Uses same threadId and resourceId as previous to keep memory context.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Now I'm over at my friend's house, and they have: chicken thighs, coconut milk, sweet potatoes, and some curry powder.
    // This step uses agent: chefAgent
    // const result = await chefAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_recipe_suggest_friends_house_query not implemented yet')
  },
})

const taskRecipeSuggestRecallPrevious = createStep({
  id: 'task_recipe_suggest_recall_previous',
  description: `Agent.stream called with Prompt_Index_RecallPrevious requesting recall using memoryOptions.lastMessages = 3.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // What did we cook before I went to my friends house?
    // This step uses agent: chefAgent
    // const result = await chefAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_recipe_suggest_recall_previous not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * recipe_workflow_pattern
 *
 * Sequence in index.ts showing Chef Agent receiving ingredients, producing suggestions, and recalling prior suggestions using shared memory.
 */
export const recipeWorkflowPattern = createWorkflow({
  id: 'recipe_workflow_pattern',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [taskRecipeSuggestInitialQuery, taskRecipeSuggestFriendsHouseQuery, taskRecipeSuggestRecallPrevious],
})
  .then(taskRecipeSuggestInitialQuery)
  .then(taskRecipeSuggestFriendsHouseQuery)
  .then(taskRecipeSuggestRecallPrevious)
  .commit()
