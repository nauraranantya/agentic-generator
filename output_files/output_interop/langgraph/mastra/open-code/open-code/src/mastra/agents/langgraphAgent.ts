/**
 * Agent: assistant
 * ID: langgraph_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Apply proposed file changes / update repository file contents.
 *   - : Capability enabling the agent to request file updates via external tool calls.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolUpdateFile } from '../tools'

/**
 * assistant
 * 
 * Instructions:
 * You are assistant.
 */
export const langgraphAgent = new Agent({
  id: `langgraph_agent`,
  name: `assistant`,
  instructions: `You are assistant.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolUpdateFile,
  },
})
