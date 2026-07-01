/**
 * Agent: Research Analyst
 * ID: research_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Performs general website search and retrieval.
 *   - : Uses Serper.dev API for search and rich web results.
 *   - : Reads the contents of a local file for use by agents.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { websiteSearchTool, serperDevTool } from '../tools'

/**
 * Research Analyst
 * 
 * Instructions:
 * Analyze the company website and provided description to extract insights on culture, values, and specific needs.
 */
export const researchAgent = new Agent({
  id: `research_agent`,
  name: `Research Analyst`,
  instructions: `Analyze the company website and provided description to extract insights on culture, values, and specific needs.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    websiteSearchTool,
    serperDevTool,
  },
})
