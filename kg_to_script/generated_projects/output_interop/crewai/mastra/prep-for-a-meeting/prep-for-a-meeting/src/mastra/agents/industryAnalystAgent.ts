/**
 * Agent: Industry Analyst
 * ID: industry_analyst_agent
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
 * Industry Analyst
 * 
 * Instructions:
 * Analyze the current industry trends, challenges, and opportunities.
 */
export const industryAnalystAgent = new Agent({
  id: `industry_analyst_agent`,
  name: `Industry Analyst`,
  instructions: `Analyze the current industry trends, challenges, and opportunities.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    exaSearchToolSearch,
    exaSearchToolFindSimilar,
    exaSearchToolGetContents,
  },
})
