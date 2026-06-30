/**
 * Mastra AI Instance - TravelAiSystemMastraexampleapp
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Plan Trip: 
 *   - Format Output: 
 * Objectives:
 *   - Assemble trip components: 
 */

import { Mastra } from '@mastra/core'

// Import agents
import { travelAgent, travelAnalyzer } from './agents'

// Import workflows
import { travelSubmissionWorkflow, airbnbFlowPattern, syncCsvWorkflow } from './workflows'

// Import memory instances
import { travelMemory } from './memory'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    travelAgent,
    travelAnalyzer,
  },
  workflows: {
    travelSubmissionWorkflow,
    airbnbFlowPattern,
    syncCsvWorkflow,
  },
  memory: {
    travelMemory,
  },
})
