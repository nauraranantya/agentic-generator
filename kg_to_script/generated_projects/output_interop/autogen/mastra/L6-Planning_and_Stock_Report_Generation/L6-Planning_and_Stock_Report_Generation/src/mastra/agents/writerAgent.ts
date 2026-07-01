/**
 * Agent: Writer
 * ID: writerAgent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : 
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { codingEnvironmentTool } from '../tools'

/**
 * Writer
 * 
 * Instructions:
 * Writer: write blogs based on the code execution results and take feedback from the admin to refine the blog.
 */
export const writerAgent = new Agent({
  id: `writerAgent`,
  name: `Writer`,
  instructions: `Writer: write blogs based on the code execution results and take feedback from the admin to refine the blog.`,
  model: 'openai/gpt-4-turbo',
  tools: {
    codingEnvironmentTool,
  },
})
