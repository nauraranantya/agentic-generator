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
import { siteCrawlTool, generateSpecTool } from '../tools'

// ── Workflow Steps ──

const siteCrawlSyncStepTask = createStep({
  id: 'site-crawl-sync-step:task',
  description: `Task executed by the workflow step site-crawl-sync-step. It runs the SiteCrawlTool (Firecrawl client) to extract markdown pages.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Task executed by the workflow step site-crawl-sync-step. It runs the SiteCrawlTool (Firecrawl client) to extract markdown pages.
    // This step uses tool: siteCrawlTool
    // TODO: Implement step logic
    throw new Error('site-crawl-sync-step:task not implemented yet')
  },
})

const generateSpecTask = createStep({
  id: 'generate-spec:task',
  description: `Task executed by the generate-spec step: this task iterates crawled pages, calls the agent to produce OpenAPI fragments, and then asks the agent to merge them.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // I have generated the following Open API specs: \${openapiResponses} - merge them into a single spec,
    // This step uses tool: generateSpecTool
    // TODO: Implement step logic
    throw new Error('generate-spec:task not implemented yet')
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
  steps: [siteCrawlSyncStepTask, generateSpecTask],
})
  .parallel([siteCrawlSyncStepTask, generateSpecTask])
  .commit()
