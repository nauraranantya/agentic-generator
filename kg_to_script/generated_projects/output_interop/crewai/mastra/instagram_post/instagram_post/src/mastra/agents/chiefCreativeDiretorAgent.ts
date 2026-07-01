/**
 * Agent: Chief Creative Director
 * ID: chief_creative_diretor_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Extract and summarize HTML content from websites.
 *   - : Query web search API and return ranked result snippets.
 *   - : Search Instagram content via web search for post examples and snippets.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolScrapeWebsite, toolSearchInternet, toolSearchInstagram } from '../tools'

/**
 * Chief Creative Director
 * 
 * Instructions:
 * Ensure final creative outputs are aligned with product goals; review and approve imagery.
 */
export const chiefCreativeDiretorAgent = new Agent({
  id: `chief_creative_diretor_agent`,
  name: `Chief Creative Director`,
  instructions: `Ensure final creative outputs are aligned with product goals; review and approve imagery.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolScrapeWebsite,
    toolSearchInternet,
    toolSearchInstagram,
  },
})
