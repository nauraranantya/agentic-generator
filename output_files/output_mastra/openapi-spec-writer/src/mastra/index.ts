/**
 * Mastra AI Instance - MastraSystem
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Generate OpenAPI spec from docs: Produce a merged OpenAPI specification from website documentation and optionally open a PR with the spec in a repository.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { openapiSpecGenAgent } from './agents'

// Import workflows
import { openApiSpecGenWorkflowPattern, makePrWorkflowPattern } from './workflows'

// Import memory instances
import { openApiSpecAgentMemory } from './memory'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * The deployed Mastra system that coordinates agents, tools and workflows for generating OpenAPI specs and creating PRs.
 */
export const mastra = new Mastra({
  agents: {
    openapiSpecGenAgent,
  },
  workflows: {
    openApiSpecGenWorkflowPattern,
    makePrWorkflowPattern,
  },
  memory: {
    openApiSpecAgentMemory,
  },
})
