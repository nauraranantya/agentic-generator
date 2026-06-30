/**
 * Mastra AI Instance - JobPostingCrewTeam
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Hiring Goal: Goal: hire for the specified hiring needs (e.g., Production Assistant for TV production in Los Angeles, June 2025) using a compelling job posting aligned with company values.
 * Objectives:
 *   - Create Job Posting Objective: Collective objective: produce a job posting that aligns with company culture and hiring needs.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { researchAgent, writerAgent, reviewAgent } from './agents'

// Import workflows
import { jobPostingWorkflow } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    researchAgent,
    writerAgent,
    reviewAgent,
  },
  workflows: {
    jobPostingWorkflow,
  },
})
