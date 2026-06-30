/**
 * Mastra AI Instance - AiCrewforscreenwriting
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - : Decide whether a text is spam or contains vulgar language and should be filtered (STOP signal).
 *   - : Analyze discussion, create dialogue-heavy screenplay and format according to requested template.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { spamfilter, analyst, scriptwriter, formatter, scorer } from './agents'

// Import workflows
import { workflowPatternScreenplay } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Team that orchestrates the sequence of agents to convert a newsgroup post into a formatted screenplay.
 */
export const mastra = new Mastra({
  agents: {
    spamfilter,
    analyst,
    scriptwriter,
    formatter,
    scorer,
  },
  workflows: {
    workflowPatternScreenplay,
  },
})
