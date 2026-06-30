/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - : Goal: exercise agent-to-agent communication via A2A protocol, fetch research, and create an engaging blog introduction from the research.
 * Objectives:
 *   - : Objective assigned to the team: gather research on agent networks and produce engaging content. Tasks ResearchTask and ContentTask contribute to this objective.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { myAgent, contentCreatorAgent } from './agents'

// Import workflows
import { a2AExamplePattern } from './workflows'

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
