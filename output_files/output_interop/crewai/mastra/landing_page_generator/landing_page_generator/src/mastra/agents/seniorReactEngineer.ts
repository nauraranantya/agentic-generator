/**
 * Agent: Senior React Engineer
 * ID: senior_react_engineer
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
import { searchInternetTool, scrapeWebsiteTool, writeFileTool, learnTemplatesTool, copyTemplateTool, readFileTool, listDirectoryTool } from '../tools'

/**
 * Senior React Engineer
 * 
 * Instructions:
 * Select a Tailwind template that fits the idea and copy it into the working folder; then update components.
 */
export const seniorReactEngineer = new Agent({
  id: `senior_react_engineer`,
  name: `Senior React Engineer`,
  instructions: `Select a Tailwind template that fits the idea and copy it into the working folder; then update components.`,
  model: 'openai/gpt-4',
  tools: {
    searchInternetTool,
    scrapeWebsiteTool,
    writeFileTool,
    learnTemplatesTool,
    copyTemplateTool,
    readFileTool,
    listDirectoryTool,
  },
})
