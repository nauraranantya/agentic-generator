/**
 * Agent: commit_message_generator
 * ID: DaneCommitMessage
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Browse and scrape web pages, return extracted text.
 *   - : Run web search queries and return result links.
 *   - : Read and list calendar events.
 *   - : Crawl websites and sync content to a DB.
 *   - : Execute system commands and capture output.
 *   - : Filesystem read/write operations.
 *   - : Generate images from text prompts and write files.
 *   - : Extract text content from PDF files.
 *   - : Build pnpm packages in given paths.
 *   - : Detect packages that will be published.
 *   - : Publish changesets to the registry.
 *   - : Set active distribution tags for published packages.
 *   - : Post messages to Slack channels via MCP client.
 *   - : Query and post to GitHub (pull requests, issues, labels, comments).
 *   - : Key-value storage for agent memory/context windows.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolFsTool } from '../tools'

/**
 * commit_message_generator
 * 
 * Instructions:
 * You are commit_message_generator.
 */
export const daneCommitMessage = new Agent({
  id: `DaneCommitMessage`,
  name: `commit_message_generator`,
  instructions: `You are commit_message_generator.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolFsTool,
  },
})
