/**
 * Workflow: openApiSpecGenWorkflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow that crawls a URL and generates an OpenAPI spec from crawled documentation.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import tools used by workflow steps
import { siteCrawlTool } from '../tools/siteCrawlTool'
import { generateSpecTool } from '../tools/generateSpecTool'

// ── Workflow Steps ──

const siteCrawlWorkflowStep = createStep({
  id: 'site-crawl-sync-step',
  description: `Step that executes a site crawl and returns crawlData and entityType.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Task executed by the workflow step site-crawl-sync-step. It runs the SiteCrawlTool (Firecrawl client) to extract markdown pages.
    // This step uses tool: siteCrawlTool
    // TODO: Implement step logic
    throw new Error('site-crawl-sync-step not implemented yet')
  },
})

const generateSpecWorkflowStep = createStep({
  id: 'generate-spec-step',
  description: `Step that generates a merged OpenAPI spec from crawled data using an agent.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // I have generated the following Open API specs: \${openapiResponses} - merge them into a single spec,
    // This step uses tool: generateSpecTool
    // TODO: Implement step logic
    throw new Error('generate-spec-step not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * openApiSpecGenWorkflow
 *
 * Workflow that crawls a URL and generates an OpenAPI spec from crawled documentation.
 */
export const openApiSpecGenWorkflowPattern = createWorkflow({
  id: 'openApiSpecGenWorkflow',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [siteCrawlWorkflowStep, generateSpecWorkflowStep],
})
  .then(siteCrawlWorkflowStep)
  .then(generateSpecWorkflowStep)
  .commit()
