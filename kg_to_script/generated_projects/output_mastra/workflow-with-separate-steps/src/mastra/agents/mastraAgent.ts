/**
 * Agent: workflow-executor
 * ID: mastra-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : 
 */

import { Agent } from '@mastra/core/agent'

/**
 * workflow-executor
 * 
 * Instructions:
 * You are workflow-executor.
 */
export const mastraAgent = new Agent({
  id: `mastra-agent`,
  name: `workflow-executor`,
  instructions: `You are workflow-executor.`,
  model: 'openai/gpt-4o-mini',
})
