/**
 * Agent: Meta Reviewer
 * ID: meta-reviewer-1
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : Objective: produce initial blogpost draft to be reviewed and refined.
 */

import { Agent } from '@mastra/core/agent'

/**
 * Meta Reviewer
 * 
 * Instructions:
 * You are Meta Reviewer.
 */
export const metaReviewer1 = new Agent({
  id: `meta-reviewer-1`,
  name: `Meta Reviewer`,
  instructions: `You are Meta Reviewer.`,
  model: 'openai/gpt-3.5-turbo',
})
