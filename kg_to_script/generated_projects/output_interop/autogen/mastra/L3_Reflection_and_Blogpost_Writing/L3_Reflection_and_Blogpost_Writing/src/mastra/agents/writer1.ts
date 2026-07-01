/**
 * Agent: Writer
 * ID: writer-1
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : Objective: produce initial blogpost draft to be reviewed and refined.
 */

import { Agent } from '@mastra/core/agent'

/**
 * Writer
 * 
 * Instructions:
 * You are Writer.
 */
export const writer1 = new Agent({
  id: `writer-1`,
  name: `Writer`,
  instructions: `You are Writer.`,
  model: 'openai/gpt-4o-mini',
})
