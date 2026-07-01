/**
 * Agent: Matcher
 * ID: matcher
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Capability to read file contents from disk.
 *   - : Capability to search and query CSV-formatted job listings.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolFileRead, toolCsvSearch } from '../tools'

/**
 * Matcher
 * 
 * Instructions:
 * Match the CV to the job opportunities based on skills, experience, and key achievements.
 */
export const matcher = new Agent({
  id: `matcher`,
  name: `Matcher`,
  instructions: `Match the CV to the job opportunities based on skills, experience, and key achievements.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolFileRead,
    toolCsvSearch,
  },
})
