/**
 * Agent: Review and Editing Specialist
 * ID: review_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - Create Job Posting Objective: Collective objective: produce a job posting that aligns with company culture and hiring needs.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { websiteSearchTool, serperDevTool, fileReadTool } from '../tools'

/**
 * Review and Editing Specialist
 * 
 * Instructions:
 * Role: Review and Editing Specialist
 */
export const reviewAgent = new Agent({
  id: `review_agent`,
  name: `Review and Editing Specialist`,
  instructions: `Role: Review and Editing Specialist`,
  model: 'openai/gpt-4o-mini',
  tools: {
    websiteSearchTool,
    serperDevTool,
    fileReadTool,
  },
})
