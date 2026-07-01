/**
 * Agent: planner-executor LLM agent (coordinates planning and performs file updates via tools and UI prompts)
 * ID: open-code-agent-001
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - planning: Generate and maintain plan lists (executed, rejected, remaining) and choose next plan item.
 *   - file update: Prepare file content updates based on plan items and perform write actions (via a tool).
 *   - UI interaction / propose changes: Push UI items to present proposed changes to a human and capture approvals or rejections.
 */

import { Agent } from '@mastra/core/agent'

// Import memory
import { openCodeMemory } from '../memory'

/**
 * planner-executor LLM agent (coordinates planning and performs file updates via tools and UI prompts)
 * 
 * Instructions:
 * You are planner-executor LLM agent (coordinates planning and performs file updates via tools and UI prompts).
 */
export const openCodeAgent001 = new Agent({
  id: `open-code-agent-001`,
  name: `planner-executor LLM agent (coordinates planning and performs file updates via tools and UI prompts)`,
  instructions: `You are planner-executor LLM agent (coordinates planning and performs file updates via tools and UI prompts).`,
  model: 'openai/gpt-4o-mini',
  memory: openCodeMemory,
})
