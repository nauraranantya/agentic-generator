/**
 * Agent: Email Assistant
 * ID: email-assistant-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Produces an email object with subject, body, and recipient based on conversation history or user edits.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolWriteEmail } from '../tools'

/**
 * Email Assistant
 * 
 * Instructions:
 * You are Email Assistant.
 */
export const emailAssistantAgent = new Agent({
  id: `email-assistant-agent`,
  name: `Email Assistant`,
  instructions: `You are Email Assistant.`,
  model: 'openai/gpt-4o',
  tools: {
    toolWriteEmail,
  },
})
