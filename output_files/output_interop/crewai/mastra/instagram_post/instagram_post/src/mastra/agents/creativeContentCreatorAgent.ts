/**
 * Agent: Creative Content Creator
 * ID: creative_content_creator_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - Copy Crew Objective: Generate analysis-informed ad copy and campaign strategy to drive engagement.
 *   - Image Crew Objective: Create photograph concepts aligned with ad copy and campaign to produce visuals for Instagram.
 * Capabilities:
 *   - web scraping: Capability to scrape and summarize website content.
 *   - internet search: Capability to search the internet and summarize results.
 *   - instagram search: Capability to search Instagram posts (site:instagram.com queries).
 *   - strategy planning: Capability to synthesize analysis into marketing strategies.
 *   - copywriting: Capability to craft punchy Instagram ad copy.
 *   - photography review: Capability to evaluate and revise photograph concepts.
 *   - review & approval: Capability to review outputs, approve, and delegate follow-ups.
 */

import { Agent } from '@mastra/core/agent'

/**
 * Creative Content Creator
 * 
 * Instructions:
 * Agent backstory and role description for Creative Content Creator
 */
export const creativeContentCreatorAgent = new Agent({
  id: `creative_content_creator_agent`,
  name: `Creative Content Creator`,
  instructions: `Agent backstory and role description for Creative Content Creator`,
  model: 'openai/gpt-4o-mini',
})
