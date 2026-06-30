/**
 * Mastra AI Instance - UnnamedProject
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import workflows
import { textUtilitiesWorkflowPattern } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * A small collection of text-processing utilities used within an agent-based solution. Contains implementations for capitalizing text and formatting message arrays into a serialized string.
 */
export const mastra = new Mastra({
  workflows: {
    textUtilitiesWorkflowPattern,
  },
})
