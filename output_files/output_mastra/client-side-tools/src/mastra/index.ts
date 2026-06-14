/**
 * Mastra AI Instance - ClientApplication(vite+React)Team
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { agentFrontend } from './agents/agentFrontend'
import { agentBackend } from './agents/agentBackend'

// Import workflows
import { streamingWorkflow } from './workflows/streamingWorkflow'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Represents the client-side application that coordinates a human user, one or more agents, and client-side tools. It contains system-level configuration for the Mastra client (baseUrl) and references the workflow used for streaming interactions.
 */
export const mastra = new Mastra({
  agents: {
    agentFrontend,
    agentBackend,
  },
  workflows: {
    streamingWorkflow,
  },
})
