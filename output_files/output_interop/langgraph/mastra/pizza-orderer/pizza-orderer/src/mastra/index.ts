/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Order Pizza Goal: Top-level intent: find a pizza shop and place a pizza order for a user.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { pizzaOrdererV1 } from './agents'

// Import workflows
import { orderPizzaGraph } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    pizzaOrdererV1,
  },
  workflows: {
    orderPizzaGraph,
  },
})
