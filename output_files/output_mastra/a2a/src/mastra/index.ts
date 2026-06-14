/**
 * Mastra AI Instance - MastraExampleTeam(a2aExample)
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { myAgent } from './agents/myAgent'
import { contentCreatorAgent } from './agents/contentCreatorAgent'

// Import workflows
import { a2AExamplePattern } from './workflows/a2AExamplePattern'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * A small two-agent system instantiated in the example code demonstrating agent-to-agent (A2A) communication: one agent performs research and another transforms research into content. The Mastra client baseUrl default (http://localhost:4111) is recorded in the system config.
 */
export const mastra = new Mastra({
  agents: {
    myAgent,
    contentCreatorAgent,
  },
  workflows: {
    a2AExamplePattern,
  },
})
