/**
 * Agent: Research Analyst
 * ID: research_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - Create Job Posting Objective: Collective objective: produce a job posting that aligns with company culture and hiring needs.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { websiteSearchTool, serperDevTool } from '../tools'

/**
 * Research Analyst
 * 
 * Instructions:
 * Role: Research Analyst
 */
export const researchAgent = new Agent({
  id: `research_agent`,
  name: `Research Analyst`,
  instructions: `Role: Research Analyst`,
  model: 'openai/gpt-4o-mini',
  tools: {
    websiteSearchTool,
    serperDevTool,
  },
})
