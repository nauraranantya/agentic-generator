/**
 * Agent: Candidate Outreach Strategist
 * ID: communicator
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
 * Candidate Outreach Strategist
 * 
 * Instructions:
 * Agent goal: create outreach templates and communication plans.
 */
export const communicator = new Agent({
  id: `communicator`,
  name: `Candidate Outreach Strategist`,
  instructions: `Agent goal: create outreach templates and communication plans.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolSerperdev,
    toolScrapeWebsite,
  },
})
