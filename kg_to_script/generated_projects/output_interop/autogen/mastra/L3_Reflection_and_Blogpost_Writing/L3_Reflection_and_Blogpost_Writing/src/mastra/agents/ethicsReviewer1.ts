/**
 * Agent: Ethics Reviewer
 * ID: ethics-reviewer-1
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : Objective: produce initial blogpost draft to be reviewed and refined.
 */

import { Agent } from '@mastra/core/agent'

/**
 * Ethics Reviewer
 * 
 * Instructions:
 * You are Ethics Reviewer.
 */
export const ethicsReviewer1 = new Agent({
  id: `ethics-reviewer-1`,
  name: `Ethics Reviewer`,
  instructions: `You are Ethics Reviewer.`,
  model: 'openai/gpt-3.5-turbo',
})
