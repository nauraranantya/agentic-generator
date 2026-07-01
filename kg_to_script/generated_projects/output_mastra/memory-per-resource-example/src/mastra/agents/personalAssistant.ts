/**
 * Agent: Personal Assistant
 * ID: personal-assistant
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : 
 * Capabilities:
 *   - conversational: Capability to hold a multi-turn conversation and respond to user inputs.
 *   - memory_update: Capability to update and persist working memory based on conversation content; expects <working_memory> tags to be used in outputs.
 *   - greet_returning_user: Capability to detect returning users and greet them referencing remembered information.
 */

import { Agent } from '@mastra/core/agent'

// Import memory
import { memoryDemo } from '../memory'

/**
 * Personal Assistant
 * 
 * Instructions:
 * Agent instructions configured at creation time (Agent.instructions in source code).
 */
export const personalAssistant = new Agent({
  id: `personal-assistant`,
  name: `Personal Assistant`,
  instructions: `Agent instructions configured at creation time (Agent.instructions in source code).`,
  model: 'openai/gpt-4o-mini',
  memory: memoryDemo,
})
