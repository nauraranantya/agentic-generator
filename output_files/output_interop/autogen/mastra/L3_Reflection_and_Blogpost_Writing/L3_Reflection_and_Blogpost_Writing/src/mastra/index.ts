/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - : Goal: create a concise (within 100 words) blogpost about DeepLearning.AI and refine it via a reflection process with multiple reviewers.
 * Objectives:
 *   - : Objective: produce initial blogpost draft to be reviewed and refined.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { writer1, critic1, seoReviewer1, legalReviewer1, ethicsReviewer1, metaReviewer1 } from './agents'

// Import workflows
import { workflowReflectionBlogpost } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    writer1,
    critic1,
    seoReviewer1,
    legalReviewer1,
    ethicsReviewer1,
    metaReviewer1,
  },
  workflows: {
    workflowReflectionBlogpost,
  },
})
