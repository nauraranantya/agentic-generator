/**
 * Agent: Planner
 * ID: plannerAgent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : 
 */

import { Agent } from '@mastra/core/agent'

/**
 * Planner
 * 
 * Instructions:
 * Planner. Given a task, determine what information is needed to complete the task. After each step is done by others, check the progress and instruct the remaining steps
 */
export const plannerAgent = new Agent({
  id: `plannerAgent`,
  name: `Planner`,
  instructions: `Planner. Given a task, determine what information is needed to complete the task. After each step is done by others, check the progress and instruct the remaining steps`,
  model: 'openai/gpt-4-turbo',
})
