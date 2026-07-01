/**
 * Agent: todolist manager
 * ID: todo-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : Ensure tasks have an estimated duration to help with planning and prioritization.
 *   - : Guarantee that the user's todo list state is saved every interaction, per agent instruction.
 * Capabilities:
 *   - manage todo list: Ability to create, update, list, and complete todo items.
 *   - timebox tasks: Ability to ask the user for estimated durations and enforce timeboxing of tasks.
 *   - save memory every response: Requirement to persist working memory in every interaction to prevent forgetting between turns.
 *   - format and render list with emojis and subtasks: Ability to render todo lists with emojis, date fields, indexed titles, descriptions, statuses, and nested subtasks using boxed bullet lists.
 */

import { Agent } from '@mastra/core/agent'

// Import memory
import { todoMemory } from '../memory'

/**
 * todolist manager
 * 
 * Instructions:
 * You are todolist manager.
 */
export const todoAgent = new Agent({
  id: `todo-agent`,
  name: `todolist manager`,
  instructions: `You are todolist manager.`,
  model: 'openai/gpt-4o-mini',
  memory: todoMemory,
})
