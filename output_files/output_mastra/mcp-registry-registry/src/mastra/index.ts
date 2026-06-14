/**
 * Mastra AI Instance - MastraRuntime
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { mcpRegistryAgent } from './agents/mcpRegistryAgent'

// Import workflows
import { mastraSimpleWorkflow } from './workflows/mastraSimpleWorkflow'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Mastra configured with a single MCP Registry Agent and a Pino logger. This Team represents the runtime composition (agents, system configuration).
 */
export const mastra = new Mastra({
  agents: {
    mcpRegistryAgent,
  },
  workflows: {
    mastraSimpleWorkflow,
  },
})
