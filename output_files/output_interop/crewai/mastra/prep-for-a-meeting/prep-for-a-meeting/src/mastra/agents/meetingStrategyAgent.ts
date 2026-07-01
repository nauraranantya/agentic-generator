/**
 * Agent: Meeting Strategy Advisor
 * ID: meeting_strategy_agent
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
 * Meeting Strategy Advisor
 * 
 * Instructions:
 * Develop talking points, questions, and strategic angles for the meeting.
 */
export const meetingStrategyAgent = new Agent({
  id: `meeting_strategy_agent`,
  name: `Meeting Strategy Advisor`,
  instructions: `Develop talking points, questions, and strategic angles for the meeting.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    exaSearchToolSearch,
    exaSearchToolFindSimilar,
    exaSearchToolGetContents,
  },
})
