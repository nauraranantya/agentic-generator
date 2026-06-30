/**
 * Agent: Executor
 * ID: executorAgent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : 
 */

import { Agent } from '@mastra/core/agent'

/**
 * Executor
 * 
 * Instructions:
 * Executor: execute code and return execution results (no human input).
 */
export const executorAgent = new Agent({
  id: `executorAgent`,
  name: `Executor`,
  instructions: `Executor: execute code and return execution results (no human input).`,
  model: 'openai/gpt-4-turbo',
})
