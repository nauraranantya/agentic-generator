/**
 * Mastra AI Instance - MastraSystem
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Environments:
 *   -  (): 
 */

import { Mastra } from '@mastra/core'

// Import agents
import { catOne } from './agents'

// Import workflows
import { sequentialWorkflowPattern, parallelWorkflowPattern, branchedWorkflowPattern, cyclicalWorkflowPattern } from './workflows'

// Import memory instances
import { catOneMemory } from './memory'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    catOne,
  },
  workflows: {
    sequentialWorkflowPattern,
    parallelWorkflowPattern,
    branchedWorkflowPattern,
    cyclicalWorkflowPattern,
  },
  memory: {
    catOneMemory,
  },
})
