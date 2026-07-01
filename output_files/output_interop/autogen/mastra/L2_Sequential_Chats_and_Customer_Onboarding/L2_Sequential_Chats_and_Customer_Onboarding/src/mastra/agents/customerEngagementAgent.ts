/**
 * Agent: customer_engagement
 * ID: Customer Engagement Agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

/**
 * customer_engagement
 * 
 * Instructions:
 * Provide engaging and fun content based on customer's info and topic preferences.
 */
export const customerEngagementAgent = new Agent({
  id: `Customer Engagement Agent`,
  name: `customer_engagement`,
  instructions: `Provide engaging and fun content based on customer's info and topic preferences.`,
  model: 'openai/gpt-4o-mini',
})
