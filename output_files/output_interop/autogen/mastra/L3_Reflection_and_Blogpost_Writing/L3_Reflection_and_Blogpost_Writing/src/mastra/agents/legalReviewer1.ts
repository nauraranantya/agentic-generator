/**
 * Agent: Legal Reviewer
 * ID: legal-reviewer-1
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : Objective: produce initial blogpost draft to be reviewed and refined.
 */

import { Agent } from '@mastra/core/agent'

/**
 * Legal Reviewer
 * 
 * Instructions:
 * You are Legal Reviewer.
 */
export const legalReviewer1 = new Agent({
  id: `legal-reviewer-1`,
  name: `Legal Reviewer`,
  instructions: `You are Legal Reviewer.`,
  model: 'openai/gpt-3.5-turbo',
})
