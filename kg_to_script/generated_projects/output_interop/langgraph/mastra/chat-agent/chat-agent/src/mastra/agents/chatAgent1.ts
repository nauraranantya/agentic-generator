/**
 * Agent: conversational assistant
 * ID: chat-agent-1
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

/**
 * conversational assistant
 * 
 * Instructions:
 * This system role message is prepended to every model invocation in the chat node.
 */
export const chatAgent1 = new Agent({
  id: `chat-agent-1`,
  name: `conversational assistant`,
  instructions: `This system role message is prepended to every model invocation in the chat node.`,
  model: 'openai/gpt-4o-mini',
})
