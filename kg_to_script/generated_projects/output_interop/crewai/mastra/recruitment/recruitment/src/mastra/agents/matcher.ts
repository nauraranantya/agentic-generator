/**
 * Agent: Candidate Matcher and Scorer
 * ID: matcher
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Capability to query search APIs and return structured search results.
 *   - : Capability to extract information from web pages using DOM parsing.
 *   - : Capability to query LinkedIn search results and format profile summaries.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolSerperdev, toolScrapeWebsite } from '../tools'

/**
 * Candidate Matcher and Scorer
 * 
 * Instructions:
 * Agent goal: evaluate and rank candidates against job requirements.
 */
export const matcher = new Agent({
  id: `matcher`,
  name: `Candidate Matcher and Scorer`,
  instructions: `Agent goal: evaluate and rank candidates against job requirements.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolSerperdev,
    toolScrapeWebsite,
  },
})
