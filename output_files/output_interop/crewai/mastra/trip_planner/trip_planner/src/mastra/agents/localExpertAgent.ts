/**
 * Agent: Local Expert at this city
 * ID: local_expert_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Analyze and compare cities by weather conditions, events, and travel costs; deliver a detailed city selection report.
 *   - : Collect and synthesize local cultural, tourism and attraction information into a comprehensive guide.
 *   - : Generate optimized daily travel itineraries with logistics, budget calculations, and packing recommendations.
 *   - : Search the internet for relevant results and return structured snippets with title, link, and snippet text.
 *   - : Scrape raw HTML of a website, partition and summarize content with an internal summarization agent; returns concise summaries for each chunk.
 *   - : Perform safe arithmetic evaluation of mathematical expressions (supports + - * / % ** and parentheses). Returns numeric result or error message.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { searchTools, browserTools } from '../tools'

/**
 * Local Expert at this city
 * 
 * Instructions:
 * Role: Local Expert; purpose: compile an in-depth city guide with hidden gems and local insights.
 */
export const localExpertAgent = new Agent({
  id: `local_expert_agent`,
  name: `Local Expert at this city`,
  instructions: `Role: Local Expert; purpose: compile an in-depth city guide with hidden gems and local insights.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    searchTools,
    browserTools,
  },
})
