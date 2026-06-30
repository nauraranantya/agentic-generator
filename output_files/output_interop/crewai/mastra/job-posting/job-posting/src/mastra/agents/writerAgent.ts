/**
 * Agent: Job Description Writer
 * ID: writer_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - Create Job Posting Objective: Collective objective: produce a job posting that aligns with company culture and hiring needs.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { websiteSearchTool, serperDevTool, fileReadTool } from '../tools'

/**
 * Job Description Writer
 * 
 * Instructions:
 * Role: Job Description Writer
 */
export const writerAgent = new Agent({
  id: `writer_agent`,
  name: `Job Description Writer`,
  instructions: `Role: Job Description Writer`,
  model: 'openai/gpt-4o-mini',
  tools: {
    websiteSearchTool,
    serperDevTool,
    fileReadTool,
  },
})
