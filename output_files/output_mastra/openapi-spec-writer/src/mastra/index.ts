/**
 * Mastra AI Instance - MastraSystem
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { openApiSpecAgent } from './agents/openApiSpecAgent'

// Import workflows
import { openApiSpecGenWorkflowPattern } from './workflows/openApiSpecGenWorkflowPattern'
import { makePrWorkflowPattern } from './workflows/makePrWorkflowPattern'

// Import memory instances
import { openApiSpecAgentMemory } from './memory/openApiSpecAgentMemory'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * The deployed Mastra system that coordinates agents, tools and workflows for generating OpenAPI specs and creating PRs.
 */
export const mastra = new Mastra({
  agents: {
    openApiSpecAgent,
  },
  workflows: {
    openApiSpecGenWorkflowPattern,
    makePrWorkflowPattern,
  },
  memory: {
    openApiSpecAgentMemory,
  },
})
