/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - : Define agent 1 goal here
 *   - : Define agent 2 goal here
 */

import { Mastra } from '@mastra/core'

// Import agents
import { agent1Name, agent2Name } from './agents'

// Import workflows
import { customCrewWorkflow } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * A Crew defined in main.py that composes two custom agents and two custom tasks. Verbose=True, debug default False.
 */
export const mastra = new Mastra({
  agents: {
    agent1Name,
    agent2Name,
  },
  workflows: {
    customCrewWorkflow,
  },
})
