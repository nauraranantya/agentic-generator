/**
 * Agent: Job Description Writer
 * ID: writer_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Performs general website search and retrieval.
 *   - : Uses Serper.dev API for search and rich web results.
 *   - : Reads the contents of a local file for use by agents.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { websiteSearchTool, serperDevTool, fileReadTool } from '../tools'

/**
 * Job Description Writer
 * 
 * Instructions:
 * Use insights from the Research Analyst to create a detailed, engaging, and enticing job posting.
 */
export const writerAgent = new Agent({
  id: `writer_agent`,
  name: `Job Description Writer`,
  instructions: `Use insights from the Research Analyst to create a detailed, engaging, and enticing job posting.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    websiteSearchTool,
    serperDevTool,
    fileReadTool,
  },
})
