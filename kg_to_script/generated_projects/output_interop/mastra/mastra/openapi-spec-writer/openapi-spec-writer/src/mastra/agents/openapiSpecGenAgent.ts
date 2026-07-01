/**
 * Agent: openapi-spec-writer
 * ID: openapi-spec-gen-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Crawls a website and extracts markdown content for downstream processing.
 *   - : Generates OpenAPI specification fragments from documentation pages and merges them.
 *   - : Formats YAML, creates branch, commits files and opens a pull request on GitHub.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolSiteCrawl, toolGenerateSpec, toolAddToGithub } from '../tools'

/**
 * openapi-spec-writer
 * 
 * Instructions:
 * You are openapi-spec-writer.
 */
export const openapiSpecGenAgent = new Agent({
  id: `openapi-spec-gen-agent`,
  name: `openapi-spec-writer`,
  instructions: `You are openapi-spec-writer.`,
  model: 'openai/gpt-3.5-turbo',
  tools: {
    toolSiteCrawl,
    toolGenerateSpec,
    toolAddToGithub,
  },
})
