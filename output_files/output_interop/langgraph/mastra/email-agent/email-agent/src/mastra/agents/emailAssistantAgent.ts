/**
 * Agent: email_assistant
 * ID: email-assistant-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - Compose Email: Generate a draft email (subject, body, to) from conversation history.
 *   - Rewrite Email: Rewrite email content given user's response/instructions; should only change requested fields.
 *   - Send Email: Finalize and send the composed email (in this implementation it yields a confirmation message indicating successful send).
 *   - Handle Human Interrupt: Present the email to a human for review and accept/edit/ignore/response and handle the resulting input accordingly.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { writeEmailTool } from '../tools'

/**
 * email_assistant
 * 
 * Instructions:
 * You are email_assistant.
 */
export const emailAssistantAgent = new Agent({
  id: `email-assistant-agent`,
  name: `email_assistant`,
  instructions: `You are email_assistant.`,
  model: 'openai/gpt-4o',
  tools: {
    writeEmailTool,
  },
})
