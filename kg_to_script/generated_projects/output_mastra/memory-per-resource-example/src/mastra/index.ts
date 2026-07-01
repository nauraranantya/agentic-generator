/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - : 
 * Objectives:
 *   - : 
 */

import { Mastra } from '@mastra/core'

// Import agents
import { personalAssistant } from './agents'

// Import workflows
import { perResourceWorkingMemoryPattern } from './workflows'

// Import memory instances
import { memoryDemo } from './memory'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    personalAssistant,
  },
  workflows: {
    perResourceWorkingMemoryPattern,
  },
  memory: {
    memoryDemo,
  },
})
