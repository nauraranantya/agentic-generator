/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { stockAgent } from './agents'

// Import workflows
import { fetchStockPricePattern } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * The runtime/host system that registers and exposes agents (in source: new Mastra({ agents: { stockAgent } })). This representation models the system logically as a Team that contains agent members and workflow patterns.
 */
export const mastra = new Mastra({
  agents: {
    stockAgent,
  },
  workflows: {
    fetchStockPricePattern,
  },
})
