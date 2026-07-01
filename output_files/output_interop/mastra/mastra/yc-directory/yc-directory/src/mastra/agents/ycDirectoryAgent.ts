/**
 * Agent: directory
 * ID: YC Directory Agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Returns an array of company records with fields: name, longDescription, tags, industries, batch.
 *   - : Ability to answer questions using the 2024 YC directory dataset.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { ycDirectoryTool } from '../tools'

/**
 * directory
 * 
 * Instructions:
 * You are directory.
 */
export const ycDirectoryAgent = new Agent({
  id: `YC Directory Agent`,
  name: `directory`,
  instructions: `You are directory.`,
  model: 'anthropic/claude-3-5-sonnet-latest',
  tools: {
    ycDirectoryTool,
  },
})
