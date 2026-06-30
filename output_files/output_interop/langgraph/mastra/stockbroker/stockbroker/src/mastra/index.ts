/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Get stock information and perform trades: Goal: Provide stock price information to the user, show portfolio details on request, and facilitate buy orders when requested by user.
 * Environments:
 *   - Trading Environment (virtual): Operational environment context for the Stockbroker agent (uses external financial datasets API).
 */

import { Mastra } from '@mastra/core'

// Import agents
import { stockbroker01 } from './agents'

// Import workflows
import { stockbrokerWorkflow } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    stockbroker01,
  },
  workflows: {
    stockbrokerWorkflow,
  },
})
