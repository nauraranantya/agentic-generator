/**
 * Agent: Matcher
 * ID: matcher
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : Objective for producing a structured summary of the given CV.
 *   - : Objective for producing a ranked list of job matches for the candidate.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { fileReadTool, csvSearchTool } from '../tools'

/**
 * Matcher
 * 
 * Instructions:
 * Agent-level prompt to orient behavior. Use CSVSearchTool and FileReadTool to access jobs CSV and CV summary.
 */
export const matcher = new Agent({
  id: `matcher`,
  name: `Matcher`,
  instructions: `Agent-level prompt to orient behavior. Use CSVSearchTool and FileReadTool to access jobs CSV and CV summary.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    fileReadTool,
    csvSearchTool,
  },
})
