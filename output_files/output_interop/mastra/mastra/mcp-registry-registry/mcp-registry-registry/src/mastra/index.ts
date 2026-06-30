/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Objectives:
 *   - : Objective for the MCP Registry Agent and Team: enable searching and retrieving MCP registry information by ID, tag, or name.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { mcpRegistryAgent } from './agents'

// Import workflows
import { mastraSimpleWorkflow } from './workflows'

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
