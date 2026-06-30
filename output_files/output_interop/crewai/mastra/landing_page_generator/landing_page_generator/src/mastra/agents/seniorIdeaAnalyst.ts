/**
 * Agent: Senior Idea Analyst
 * ID: senior_idea_analyst
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - web search: Capability to search internet and return snippets.
 *   - web scraping and summarization: Capability to scrape a website and summarize content.
 *   - file write: Capability to write content safely to files in workdir.
 *   - learn templates listing: Capability to read templates configuration and list template options.
 *   - copy template folder: Capability to copy template folders into project workspace.
 *   - read file: Capability to read file content from the workspace.
 *   - list directory: Capability to list directories in the workspace.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { searchInternetTool, scrapeWebsiteTool } from '../tools'

/**
 * Senior Idea Analyst
 * 
 * Instructions:
 * Understand and expand the idea into a comprehensive idea report, detailing value proposition and features.
 */
export const seniorIdeaAnalyst = new Agent({
  id: `senior_idea_analyst`,
  name: `Senior Idea Analyst`,
  instructions: `Understand and expand the idea into a comprehensive idea report, detailing value proposition and features.`,
  model: 'openai/gpt-4',
  tools: {
    searchInternetTool,
    scrapeWebsiteTool,
  },
})
