/**
 * Agent: LLM Agent
 * ID: agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - Enable user-agent interactive messaging: Objective to allow a human user to send free-text messages to the agent and receive streaming responses.
 *   - Handle streaming responses and events: Objective to properly process streaming data, including tool call events, tool results, deltas, and text parts.
 *   - Apply UI updates requested via tool calls: Objective to apply client-side state changes (color, logo size, posts) as requested by tool calls from the agent.
 * Capabilities:
 *   - Change background color: Capability to change the UI color state (expects a single string property 'color').
 *   - Change logo size: Capability to change the UI logo size. Expects 'height' and 'width' string properties.
 *   - Add a new post: Capability to append a new post entry containing 'color' and 'name' to the posts collection in the client.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolChangeColor, toolChangeLogoSize, toolAddPost } from '../tools'

/**
 * LLM Agent
 * 
 * Instructions:
 * System/instruction prompt provided to the agent in mastra configuration (src/mastra/agents/index.ts).
 */
export const agent = new Agent({
  id: `agent`,
  name: `LLM Agent`,
  instructions: `System/instruction prompt provided to the agent in mastra configuration (src/mastra/agents/index.ts).`,
  model: 'openai/gpt-4o',
  tools: {
    toolChangeColor,
    toolChangeLogoSize,
    toolAddPost,
  },
})
