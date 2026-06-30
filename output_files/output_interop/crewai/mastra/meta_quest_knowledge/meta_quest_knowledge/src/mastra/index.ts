/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - : Goal expressed in agents configuration to provide best answers to questions about Meta Quest.
 * Objectives:
 *   - : Objective assigned to the crew: answer user questions by using available knowledge sources (PDF manual) and agent capabilities.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { metaQuestExpert } from './agents'

// Import workflows
import { metaQuestSequentialWorkflow } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Crew coordinating agents and tasks to answer Meta Quest questions using available knowledge sources (PDF).
 */
export const mastra = new Mastra({
  agents: {
    metaQuestExpert,
  },
  workflows: {
    metaQuestSequentialWorkflow,
  },
})
