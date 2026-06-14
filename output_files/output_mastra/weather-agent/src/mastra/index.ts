/**
 * Mastra AI Instance - MastraAgentBasedSystem
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { weatherAgent } from './agents/weatherAgent'
import { weatherReporterAgent } from './agents/weatherReporterAgent'

// Import workflows
import { wfWeatherWorkflow } from './workflows/wfWeatherWorkflow'
import { wfWeatherWorkflowWithToolAndAgent } from './workflows/wfWeatherWorkflowWithToolAndAgent'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * System coordinating weather agents, tools and workflows (Mastra instance configured with LibSQL storage and multiple workflows).
 */
export const mastra = new Mastra({
  agents: {
    weatherAgent,
    weatherReporterAgent,
  },
  workflows: {
    wfWeatherWorkflow,
    wfWeatherWorkflowWithToolAndAgent,
  },
})
