/**
 * Mastra AI Instance - MastraSystem(agentRegistry)
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { memoryAgent } from './agents/memoryAgent'

// Import workflows
import { workflowChatPattern } from './workflows/workflowChatPattern'

// Import memory instances
import { memoryKb } from './memory/memoryKb'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Represents the Mastra container in the source code that registers and exposes the 'memoryAgent' instance.
 */
export const mastra = new Mastra({
  agents: {
    memoryAgent,
  },
  workflows: {
    workflowChatPattern,
  },
  memory: {
    memoryKb,
  },
})
