/**
 * Agent: Senior Idea Analyst
 * ID: senior_idea_analyst
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Perform web search queries and return structured results.
 *   - : Scrape website HTML and summarize content into concise summaries.
 *   - : Inspect available landing page templates and surface options.
 *   - : Copy a landing page template folder into the working project directory.
 *   - : Write files to the workdir with validation and allowed extensions.
 *   - : Read files from the workdir.
 *   - : List directory contents under the workdir.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolSearchInternet, toolScrapeAndSummarizeWebsite } from '../tools'

/**
 * Senior Idea Analyst
 * 
 * Instructions:
 * Understand and expand upon the essence of ideas, make sure they are great and focus on real pain points others could benefit from.
 */
export const seniorIdeaAnalyst = new Agent({
  id: `senior_idea_analyst`,
  name: `Senior Idea Analyst`,
  instructions: `Understand and expand upon the essence of ideas, make sure they are great and focus on real pain points others could benefit from.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolSearchInternet,
    toolScrapeAndSummarizeWebsite,
  },
})
