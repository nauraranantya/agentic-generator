/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { chatAgent1 } from './agents'

// Import workflows
import { chatAgentStateGraph } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * A logical grouping used here so the workflow pattern can be linked to the agent; the original source is a single compiled agent graph.
 */
export const mastra = new Mastra({
  agents: {
    chatAgent1,
  },
  workflows: {
    chatAgentStateGraph,
  },
})
