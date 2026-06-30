/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Primary goal: Identify birds and contextual metadata: 
 * Objectives:
 *   - Acquire representative image for inspection: 
 *   - Identify bird presence/species and summarize location: 
 * Environments:
 *   - Web runtime environment (Next.js / browser + server (application) environment; uses Unsplash API via server-side call and LLM via configured model.): 
 */

import { Mastra } from '@mastra/core'

// Import agents
import { birdChecker } from './agents'

// Import workflows
import { birdCheckerWorkflow } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    birdChecker,
  },
  workflows: {
    birdCheckerWorkflow,
  },
})
