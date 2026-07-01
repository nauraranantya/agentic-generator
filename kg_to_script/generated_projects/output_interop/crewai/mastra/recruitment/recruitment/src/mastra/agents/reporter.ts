/**
 * Agent: Candidate Reporting Specialist
 * ID: reporter
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Capability to query search APIs and return structured search results.
 *   - : Capability to extract information from web pages using DOM parsing.
 *   - : Capability to query LinkedIn search results and format profile summaries.
 */

import { Agent } from '@mastra/core/agent'

/**
 * Candidate Reporting Specialist
 * 
 * Instructions:
 * Agent goal: compile findings and recommend top candidates.
 */
export const reporter = new Agent({
  id: `reporter`,
  name: `Candidate Reporting Specialist`,
  instructions: `Agent goal: compile findings and recommend top candidates.`,
  model: 'openai/gpt-4o-mini',
})
