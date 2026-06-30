/**
 * Agent: SEO Reviewer
 * ID: seo-reviewer-1
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : Objective: produce initial blogpost draft to be reviewed and refined.
 */

import { Agent } from '@mastra/core/agent'

/**
 * SEO Reviewer
 * 
 * Instructions:
 * You are SEO Reviewer.
 */
export const seoReviewer1 = new Agent({
  id: `seo-reviewer-1`,
  name: `SEO Reviewer`,
  instructions: `You are SEO Reviewer.`,
  model: 'openai/gpt-3.5-turbo',
})
