/**
 * Agent: CV Reader
 * ID: cv_reader
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : Objective for producing a structured summary of the given CV.
 *   - : Objective for producing a ranked list of job matches for the candidate.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { fileReadTool } from '../tools'

/**
 * CV Reader
 * 
 * Instructions:
 * Agent-level prompt to orient behavior. Use FileReadTool to access CV file. Produce a structured CV summary.
 */
export const cvReader = new Agent({
  id: `cv_reader`,
  name: `CV Reader`,
  instructions: `Agent-level prompt to orient behavior. Use FileReadTool to access CV file. Produce a structured CV summary.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    fileReadTool,
  },
})
