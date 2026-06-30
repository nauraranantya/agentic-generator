/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Build a Todo App: 
 * Human Agents:
 *   - human_user ()
 * Environments:
 *   - Development environment (development (file system, browser localStorage, UI)): 
 */

import { Mastra } from '@mastra/core'

// Import agents
import { openCodeAgent001 } from './agents'

// Import workflows
import { openCodeGraphPattern } from './workflows'

// Import memory instances
import { openCodeMemory } from './memory'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 */
export const mastra = new Mastra({
  agents: {
    openCodeAgent001,
  },
  workflows: {
    openCodeGraphPattern,
  },
  memory: {
    openCodeMemory,
  },
})
