/**
 * Agent: Job Candidate Researcher
 * ID: researcher
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Capability to query search APIs and return structured search results.
 *   - : Capability to extract information from web pages using DOM parsing.
 *   - : Capability to query LinkedIn search results and format profile summaries.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolSerperdev, toolScrapeWebsite, toolLinkedin } from '../tools'

/**
 * Job Candidate Researcher
 * 
 * Instructions:
 * Agent goal: find potential candidates matching provided job requirements.
 */
export const researcher = new Agent({
  id: `researcher`,
  name: `Job Candidate Researcher`,
  instructions: `Agent goal: find potential candidates matching provided job requirements.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolSerperdev,
    toolScrapeWebsite,
    toolLinkedin,
  },
})
