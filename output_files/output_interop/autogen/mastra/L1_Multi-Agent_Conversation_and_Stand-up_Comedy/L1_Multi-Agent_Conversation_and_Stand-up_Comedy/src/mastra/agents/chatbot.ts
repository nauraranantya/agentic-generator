/**
 * Agent: conversable agent
 * ID: chatbot
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Provides LLM inference and chat functionality.
 *   - : Retrieves OpenAI API key from environment or secret store.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolOpenAiApi, toolGetOpenaiApiKey } from '../tools'

/**
 * conversable agent
 * 
 * Instructions:
 * You are conversable agent.
 */
export const chatbot = new Agent({
  id: `chatbot`,
  name: `conversable agent`,
  instructions: `You are conversable agent.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolOpenAiApi,
    toolGetOpenaiApiKey,
  },
})
