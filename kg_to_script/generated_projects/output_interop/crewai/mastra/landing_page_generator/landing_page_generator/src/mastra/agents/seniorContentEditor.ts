/**
 * Agent: Senior Content Editor
 * ID: senior_content_editor
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
import { toolWriteFile } from '../tools'

/**
 * Senior Content Editor
 * 
 * Instructions:
 * Ensure the landing page content is clear, concise, and captivating.
 */
export const seniorContentEditor = new Agent({
  id: `senior_content_editor`,
  name: `Senior Content Editor`,
  instructions: `Ensure the landing page content is clear, concise, and captivating.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolWriteFile,
  },
})
