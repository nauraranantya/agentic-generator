/**
 * Mastra AI Instance - MarketingPostsCrewTeam
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Marketing project goal: Boost awareness and adoption of CrewAI's services among enterprise clients. Create a comprehensive marketing campaign focusing on ease of use, scalability, and integration capabilities.
 *   - Lead Market Analyst personal goal: Conduct amazing analysis of the products and competitors, providing in-depth insights to guide marketing strategies.
 *   - Chief Marketing Strategist personal goal: Synthesize amazing insights from product analysis to formulate incredible marketing strategies.
 *   - Creative Content Creator personal goal: Develop compelling and innovative content for social media campaigns, with a focus on creating high-impact ad copies.
 * Objectives:
 *   - Produce campaign ideas: Objective: generate creative campaign ideas for the marketing project.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { leadMarketAnalyst, chiefMarketingStrategist, creativeContentCreator } from './agents'

// Import workflows
import { marketingPostsWorkflow } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * Team that coordinates agents and tasks for the marketing_posts solution. Process executed: sequential. Agents and tasks declared in crew definition.
 */
export const mastra = new Mastra({
  agents: {
    leadMarketAnalyst,
    chiefMarketingStrategist,
    creativeContentCreator,
  },
  workflows: {
    marketingPostsWorkflow,
  },
})
