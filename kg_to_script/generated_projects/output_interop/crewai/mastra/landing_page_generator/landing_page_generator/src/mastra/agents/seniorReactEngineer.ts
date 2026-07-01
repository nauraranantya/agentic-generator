/**
 * Agent: Senior React Engineer
 * ID: senior_react_engineer
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
import { toolSearchInternet, toolScrapeAndSummarizeWebsite, toolLearnLandingPageOptions, toolCopyLandingPageTemplate, toolWriteFile, toolReadFile, toolListDirectory } from '../tools'

/**
 * Senior React Engineer
 * 
 * Instructions:
 * Build an intuitive, aesthetically pleasing, and high-converting landing page.
 */
export const seniorReactEngineer = new Agent({
  id: `senior_react_engineer`,
  name: `Senior React Engineer`,
  instructions: `Build an intuitive, aesthetically pleasing, and high-converting landing page.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolSearchInternet,
    toolScrapeAndSummarizeWebsite,
    toolLearnLandingPageOptions,
    toolCopyLandingPageTemplate,
    toolWriteFile,
    toolReadFile,
    toolListDirectory,
  },
})
