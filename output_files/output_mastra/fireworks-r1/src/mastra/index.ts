/**
 * Mastra AI Instance - MastraRuntime(exampleConfiguration)
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { exampleAgent } from './agents/exampleAgent'

// Import memory instances
import { exampleAgentMemory } from './memory/exampleAgentMemory'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Represents the Mastra runtime created by \`new Mastra({ agents: { agent }, logger: new PinoLogger(...) })\` in code. The system coordinates agents and contains system-level configuration for the logger.
 */
export const mastra = new Mastra({
  agents: {
    exampleAgent,
  },
  memory: {
    exampleAgentMemory,
  },
})
