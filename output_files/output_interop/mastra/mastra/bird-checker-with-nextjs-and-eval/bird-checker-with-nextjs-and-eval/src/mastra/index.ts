/**
 * Mastra AI Instance - MastraDeploymentBirdChecker
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Identify birds and species from images: Primary goal: determine whether images contain birds, identify species when present, and summarize the location.
 * Objectives:
 *   - Accuracy evaluation objective: Objective to measure whether the agent identifies birds and species correctly (used by evaluation).
 * Environments:
 *   - Web UI Environment (nextjs + browser UI (visualization of images, interactive tags)): Operational environment of the Bird Checker (user selects tags in UI which trigger image retrieval and agent analysis).
 */

import { Mastra } from '@mastra/core'

// Import agents
import { birdAgent } from './agents'

// Import workflows
import { birdCheckerWorkflow } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Deployment of the Bird Checker composed using Mastra: maps an agent id to a running LLM agent component.
 */
export const mastra = new Mastra({
  agents: {
    birdAgent,
  },
  workflows: {
    birdCheckerWorkflow,
  },
})
