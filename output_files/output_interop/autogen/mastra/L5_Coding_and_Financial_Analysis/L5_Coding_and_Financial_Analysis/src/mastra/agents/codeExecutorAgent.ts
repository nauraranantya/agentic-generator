/**
 * Agent: conversable code executor
 * ID: code_executor_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - Produce stock gain YTD plot objective: 
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { localCmdExecutorTool } from '../tools'

/**
 * conversable code executor
 * 
 * Instructions:
 * You are conversable code executor.
 */
export const codeExecutorAgent = new Agent({
  id: `code_executor_agent`,
  name: `conversable code executor`,
  instructions: `You are conversable code executor.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    localCmdExecutorTool,
  },
})
