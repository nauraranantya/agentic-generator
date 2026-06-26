/**
 * Agent: LLM Agent
 * ID: dane-issue-labeler
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - Execute shell commands: Running external commands via execa or child_process (e.g., git, pnpm, npm).
 *   - Filesystem read/write: Read, write and append files on local filesystem.
 *   - Web browsing and scraping: Open a headless browser, navigate to pages, extract text.
 *   - Web search: Query Google search and extract result links.
 *   - Read PDF: Extract text and metadata from PDF files.
 *   - Read local calendar: Access MacOS Calendar via AppleScript and parse events.
 *   - Build and publish packages: Run pnpm build and changeset publish, set npm dist-tags.
 *   - Post messages to Slack via MCP: Send formatted messages to Slack channels using MCP client.
 */

import { Agent } from '@mastra/core/agent'

// Import memory
import { memoryUpstash } from '../memory'

/**
 * LLM Agent
 * 
 * Instructions:
 * You are LLM Agent.
 */
export const daneIssueLabeler = new Agent({
  id: `dane-issue-labeler`,
  name: `LLM Agent`,
  instructions: `You are LLM Agent.`,
  model: 'anthropic/claude-3-5-sonnet-20241022',
  memory: memoryUpstash,
})
