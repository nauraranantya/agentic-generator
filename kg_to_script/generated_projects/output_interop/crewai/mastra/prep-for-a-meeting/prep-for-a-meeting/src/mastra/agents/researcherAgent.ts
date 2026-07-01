/**
 * Agent: Research Specialist
 * ID: researcher_agent
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
 * Research Specialist
 * 
 * Instructions:
 * Conduct thorough research on people and companies involved in the meeting.
 */
export const researcherAgent = new Agent({
  id: `researcher_agent`,
  name: `Research Specialist`,
  instructions: `Conduct thorough research on people and companies involved in the meeting.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    exaSearchToolSearch,
    exaSearchToolFindSimilar,
    exaSearchToolGetContents,
  },
})
