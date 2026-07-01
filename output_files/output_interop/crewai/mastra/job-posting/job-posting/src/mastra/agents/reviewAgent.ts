/**
 * Agent: Review and Editing Specialist
 * ID: review_agent
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
 * Review and Editing Specialist
 * 
 * Instructions:
 * Review the job posting for clarity, engagement, grammatical accuracy, and alignment with the company's culture and values.
 */
export const reviewAgent = new Agent({
  id: `review_agent`,
  name: `Review and Editing Specialist`,
  instructions: `Review the job posting for clarity, engagement, grammatical accuracy, and alignment with the company's culture and values.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    websiteSearchTool,
    serperDevTool,
    fileReadTool,
  },
})
