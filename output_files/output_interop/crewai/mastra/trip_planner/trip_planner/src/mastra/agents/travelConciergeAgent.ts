/**
 * Agent: Amazing Travel Concierge
 * ID: travel_concierge_agent
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
import { searchTools, browserTools, calculatorTools } from '../tools'

// Import memory
import { tripMemory } from '../memory'

/**
 * Amazing Travel Concierge
 * 
 * Instructions:
 * Role: Travel Concierge; purpose: produce a full 7-day itinerary, budget breakdown and packing suggestions.
 */
export const travelConciergeAgent = new Agent({
  id: `travel_concierge_agent`,
  name: `Amazing Travel Concierge`,
  instructions: `Role: Travel Concierge; purpose: produce a full 7-day itinerary, budget breakdown and packing suggestions.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    searchTools,
    browserTools,
    calculatorTools,
  },
  memory: tripMemory,
})
