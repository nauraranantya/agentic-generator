/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Objectives:
 *   - : Objective representing the evaluation goal to measure the relevancy of ycAgent answers using an automatic scorer.
 *   - : Objective requiring the agent to answer questions about companies in the YC 2024 directory using only the dataset fields: name, longDescription, tags, industries, batch.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { ycDirectoryAgent } from './agents'

// Import workflows
import { ycQueryWorkflow } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * The Mastra system instance created in src/mastra/index.ts that composes agents and a logger.
 */
export const mastra = new Mastra({
  agents: {
    ycDirectoryAgent,
  },
  workflows: {
    ycQueryWorkflow,
  },
})
