/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Lesson 5: Coding and Financial Analysis Goal: 
 * Objectives:
 *   - Produce stock gain YTD plot objective: 
 */

import { Mastra } from '@mastra/core'

// Import agents
import { codeExecutorAgent, codeWriterAgent } from './agents'

// Import workflows
import { l5CodingFinancialAnalysisPattern } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    codeExecutorAgent,
    codeWriterAgent,
  },
  workflows: {
    l5CodingFinancialAnalysisPattern,
  },
})
