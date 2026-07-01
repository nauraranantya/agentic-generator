/**
 * Agent: Industry Analyst
 * ID: industry_analyst_agent_1
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - Exa.search: Search for webpages using a query and return top results (num_results=3).
 *   - Exa.find_similar: Find webpages similar to a given URL (num_results=3).
 *   - Exa.get_contents: Retrieve page contents for a list of ids. Handles JSON or Python literal lists input;
validates input is a list of string ids; returns extracted contents (first ~1000 chars per segment).
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { exaSearchTool } from '../tools'

/**
 * Industry Analyst
 * 
 * Instructions:
 * Role: Industry Analyst; Goal: Analyze industry trends and opportunities
 */
export const industryAnalystAgent1 = new Agent({
  id: `industry_analyst_agent_1`,
  name: `Industry Analyst`,
  instructions: `Role: Industry Analyst; Goal: Analyze industry trends and opportunities`,
  model: 'openai/gpt-4o-mini',
  tools: {
    exaSearchTool,
  },
})
