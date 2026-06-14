/**
 * Mastra AI Instance - PersonalAssistantSystem
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { personalAssistant } from './agents/personalAssistant'

// Import workflows
import { perResourceWorkingMemoryPattern } from './workflows/perResourceWorkingMemoryPattern'

// Import memory instances
import { memoryDemo } from './memory/memoryDemo'

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
