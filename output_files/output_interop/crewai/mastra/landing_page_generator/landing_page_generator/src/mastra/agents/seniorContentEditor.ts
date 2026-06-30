/**
 * Agent: Senior Content Editor
 * ID: senior_content_editor
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
import { writeFileTool, readFileTool, listDirectoryTool } from '../tools'

/**
 * Senior Content Editor
 * 
 * Instructions:
 * Produce content for components, update components, and QA them according to rules.
 */
export const seniorContentEditor = new Agent({
  id: `senior_content_editor`,
  name: `Senior Content Editor`,
  instructions: `Produce content for components, update components, and QA them according to rules.`,
  model: 'openai/gpt-4',
  tools: {
    writeFileTool,
    readFileTool,
    listDirectoryTool,
  },
})
