/**
 * Mastra AI Instance - StockAnalysisCrew
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Stock analysis overall goal: Conduct stock and filings analysis pipeline that collects news, analyzes EDGAR filings, computes key financial metrics and produces investment recommendations.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { financialAgent, financialAnalystAgent, researchAnalystAgent, investmentAdvisorAgent } from './agents'

// Import workflows
import { stockAnalysisWorkflow } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Team that coordinates a set of LLM agents and tasks to perform stock/filings/research analysis for a given company ticker (example: AMZN).
 */
export const mastra = new Mastra({
  agents: {
    financialAgent,
    financialAnalystAgent,
    researchAnalystAgent,
    investmentAdvisorAgent,
  },
  workflows: {
    stockAnalysisWorkflow,
  },
})
