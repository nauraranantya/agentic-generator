/**
 * Agent: Briefing Coordinator
 * ID: summary_and_briefing_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Performs web searches and returns search result identifiers.
 *   - : Finds webpages similar to a given URL.
 *   - : Retrieves and returns contents of webpages by IDs.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { exaSearchToolSearch, exaSearchToolFindSimilar, exaSearchToolGetContents } from '../tools'

/**
 * Briefing Coordinator
 * 
 * Instructions:
 * Compile all gathered information into a concise, informative briefing document.
 */
export const summaryAndBriefingAgent = new Agent({
  id: `summary_and_briefing_agent`,
  name: `Briefing Coordinator`,
  instructions: `Compile all gathered information into a concise, informative briefing document.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    exaSearchToolSearch,
    exaSearchToolFindSimilar,
    exaSearchToolGetContents,
  },
})
