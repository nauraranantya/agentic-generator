/**
 * Mastra AI Instance - ClientApplicationViteReactTeam
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Interactive browser UI driven by agent: Goal for the client app: enable an interactive UI where the language model/agent can instruct the browser to perform UI changes and stream text responses.
 *   - Provide interactive user experience: Higher-level goal: deliver a streaming conversational experience with dynamic UI updates triggered by model-invoked tool calls.
 * Objectives:
 *   - Enable user-agent interactive messaging: Objective to allow a human user to send free-text messages to the agent and receive streaming responses.
 *   - Handle streaming responses and events: Objective to properly process streaming data, including tool call events, tool results, deltas, and text parts.
 *   - Apply UI updates requested via tool calls: Objective to apply client-side state changes (color, logo size, posts) as requested by tool calls from the agent.
 * Human Agents:
 *   - human_user ()
 */

import { Mastra } from '@mastra/core'

// Import agents
import { agent, testAgent } from './agents'

// Import workflows
import { streamingWorkflow } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Represents the client-side application that coordinates a human user, one or more agents, and client-side tools. It contains system-level configuration for the Mastra client (baseUrl) and references the workflow used for streaming interactions.
 */
export const mastra = new Mastra({
  agents: {
    agent,
    testAgent,
  },
  workflows: {
    streamingWorkflow,
  },
})
