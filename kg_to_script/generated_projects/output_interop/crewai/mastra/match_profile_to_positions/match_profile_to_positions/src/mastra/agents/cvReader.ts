/**
 * Agent: CV Reader
 * ID: cv_reader
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Capability to read file contents from disk.
 *   - : Capability to search and query CSV-formatted job listings.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolFileRead } from '../tools'

/**
 * CV Reader
 * 
 * Instructions:
 * Extract relevant information from the CV, such as skills, experience, and education.
 */
export const cvReader = new Agent({
  id: `cv_reader`,
  name: `CV Reader`,
  instructions: `Extract relevant information from the CV, such as skills, experience, and education.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolFileRead,
  },
})
