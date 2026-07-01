/**
 * Agent: assistant
 * ID: Chat Agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

/**
 * assistant
 * 
 * Instructions:
 * You are assistant.
 */
export const chatAgent = new Agent({
  id: `Chat Agent`,
  name: `assistant`,
  instructions: `You are assistant.`,
  model: 'openai/gpt-4o-mini',
})
