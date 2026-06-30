/**
 * Mastra AI Instance - CopyCrew
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Marketing Campaign Objective: Overarching objective: produce Instagram post copy and photograph concepts that highlight the product, its unique selling points, and create a high-impact campaign.
 * Objectives:
 *   - Copy Crew Objective: Generate analysis-informed ad copy and campaign strategy to drive engagement.
 *   - Image Crew Objective: Create photograph concepts aligned with ad copy and campaign to produce visuals for Instagram.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { productCompetitorAgent, strategyPlannerAgent, creativeContentCreatorAgent, seniorPhotographerAgent, chiefCreativeDirectorAgent } from './agents'

// Import workflows
import { wpCopyCrew, wpImageCrew } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    productCompetitorAgent,
    strategyPlannerAgent,
    creativeContentCreatorAgent,
    seniorPhotographerAgent,
    chiefCreativeDirectorAgent,
  },
  workflows: {
    wpCopyCrew,
    wpImageCrew,
  },
})
