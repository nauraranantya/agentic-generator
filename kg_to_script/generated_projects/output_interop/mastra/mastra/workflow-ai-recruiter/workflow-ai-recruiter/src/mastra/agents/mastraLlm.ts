/**
 * Agent: workflow-processor
 * ID: mastra-llm
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

/**
 * workflow-processor
 * 
 * Instructions:
 * You are workflow-processor.
 */
export const mastraLlm = new Agent({
  id: `mastra-llm`,
  name: `workflow-processor`,
  instructions: `You are workflow-processor.`,
  model: 'openai/gpt-4o',
})
