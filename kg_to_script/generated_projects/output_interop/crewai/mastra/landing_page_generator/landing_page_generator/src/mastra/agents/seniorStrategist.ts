/**
 * Agent: Senior Communications Strategist
 * ID: senior_strategist
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
 * Senior Communications Strategist
 * 
 * Instructions:
 * Craft compelling stories using the Golden Circle method to captivate and engage people around an idea.
 */
export const seniorStrategist = new Agent({
  id: `senior_strategist`,
  name: `Senior Communications Strategist`,
  instructions: `Craft compelling stories using the Golden Circle method to captivate and engage people around an idea.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolSearchInternet,
    toolScrapeAndSummarizeWebsite,
  },
})
