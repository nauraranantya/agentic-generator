/**
 * Agent: Chief Creative Director
 * ID: chief_creative_director_agent
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
 * Chief Creative Director
 * 
 * Instructions:
 * Agent backstory and role description for Chief Creative Director
 */
export const chiefCreativeDirectorAgent = new Agent({
  id: `chief_creative_director_agent`,
  name: `Chief Creative Director`,
  instructions: `Agent backstory and role description for Chief Creative Director`,
  model: 'openai/gpt-4o-mini',
})
