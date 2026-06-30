/**
 * Agent: Senior Communications Strategist
 * ID: senior_strategist
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
 * Senior Communications Strategist
 * 
 * Instructions:
 * Provide WHY, HOW, WHAT messaging and core message for the idea.
 */
export const seniorStrategist = new Agent({
  id: `senior_strategist`,
  name: `Senior Communications Strategist`,
  instructions: `Provide WHY, HOW, WHAT messaging and core message for the idea.`,
  model: 'openai/gpt-4',
  tools: {
    searchInternetTool,
    scrapeWebsiteTool,
  },
})
