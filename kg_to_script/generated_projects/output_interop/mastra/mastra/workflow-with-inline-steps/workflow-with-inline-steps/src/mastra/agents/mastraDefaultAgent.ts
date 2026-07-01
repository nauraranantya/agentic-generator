/**
 * Agent: workflow-executor
 * ID: mastra_default_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

/**
 * workflow-executor
 * 
 * Instructions:
 * You are workflow-executor.
 */
export const mastraDefaultAgent = new Agent({
  id: `mastra_default_agent`,
  name: `workflow-executor`,
  instructions: `You are workflow-executor.`,
  model: 'openai/gpt-4o-mini',
})
