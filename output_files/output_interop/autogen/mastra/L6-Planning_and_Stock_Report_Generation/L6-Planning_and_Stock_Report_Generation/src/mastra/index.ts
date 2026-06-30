/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - : 
 * Objectives:
 *   - : 
 * Human Agents:
 *   - admin ()
 */

import { Mastra } from '@mastra/core'

// Import agents
import { plannerAgent, engineerAgent, executorAgent, writerAgent } from './agents'

// Import workflows
import { stockReportGenerationPattern } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Represents the group chat coordinating agents: Admin (user proxy), Planner, Engineer, Executor, Writer. Modeled as a Team for lack of a dedicated GroupChat class in the ontology.
 */
export const mastra = new Mastra({
  agents: {
    plannerAgent,
    engineerAgent,
    executorAgent,
    writerAgent,
  },
  workflows: {
    stockReportGenerationPattern,
  },
})
