/**
 * Mastra AI Instance - BlogCrewIndustryspecializedagentsexample
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { biomedAgent1, healthcareAgent1, financialAgent1 } from './agents'

// Import workflows
import { blogCrewWorkflowPattern } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Crew assembled to produce industry-specific analyses of Weaviate features. Agents: BiomedicalMarketingAgent, HealthcareMarketingAgent, FinancialMarketingAgent. Tasks: one task per agent describing investigation of a given {weaviate_feature} and producing an industry-specific analysis. The Crew kickoff_for_each iterates inputs (weaviate_features) for each task; iteration is represented via feature Resource individuals (see Issues/Assumptions).
 */
export const mastra = new Mastra({
  agents: {
    biomedAgent1,
    healthcareAgent1,
    financialAgent1,
  },
  workflows: {
    blogCrewWorkflowPattern,
  },
})
