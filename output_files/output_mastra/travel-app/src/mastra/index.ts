/**
 * Mastra AI Instance - TravelaiSystem(mastraExampleApp)
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { travelAgent } from './agents/travelAgent'
import { travelAnalyzer } from './agents/travelAnalyzer'

// Import workflows
import { travelSubmissionWorkflow } from './workflows/travelSubmissionWorkflow'
import { airbnbFlowPattern } from './workflows/airbnbFlowPattern'
import { syncCsvWorkflow } from './workflows/syncCsvWorkflow'

// Import memory instances
import { travelMemory } from './memory/travelMemory'

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
