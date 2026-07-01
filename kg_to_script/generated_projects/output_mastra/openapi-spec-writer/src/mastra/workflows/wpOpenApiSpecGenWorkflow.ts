/**
 * Workflow: wp_open_api_spec_gen_workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow to crawl a site, generate OpenAPI fragments per page, then merge into a single spec.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { openapiSpecGenAgent } from '../agents'

// Import tools used by workflow steps
import { toolSiteCrawl, toolGenerateSpec } from '../tools'

// ── Workflow Steps ──

const taskSiteCrawlSync = createStep({
  id: 'task_site_crawl_sync',
  description: `Crawl a website and extract the markdown content and sync it to the database.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Crawl the provided URL, extract main content as markdown, include sourceURL in metadata. Use provided pathRegex and limit. Exclude nav/header/footer and unrelated tags; return markdown blocks and metadata.
    // This step uses tool: toolSiteCrawl
    // TODO: Implement step logic
    throw new Error('task_site_crawl_sync not implemented yet')
  },
})

const taskGenerateSpec = createStep({
  id: 'task_generate_spec',
  description: `For each crawled markdown page, ask the agent to turn it into an OpenAPI spec fragment; then ask the agent to merge fragments into a single spec.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // I have generated the following Open API specs: <list of fragments>. Merge them into a single spec and ensure the result is a valid OpenAPI YAML document. Remove code fences and unify components/paths to avoid duplicates.
    // This step uses agent: openapiSpecGenAgent
    // const result = await openapiSpecGenAgent.generate('...')
    // This step uses tool: toolGenerateSpec
    // TODO: Implement step logic
    throw new Error('task_generate_spec not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * wp_open_api_spec_gen_workflow
 *
 * Workflow to crawl a site, generate OpenAPI fragments per page, then merge into a single spec.
 */
export const wpOpenApiSpecGenWorkflow = createWorkflow({
  id: 'wp_open_api_spec_gen_workflow',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [taskSiteCrawlSync, taskGenerateSpec],
})
  .then(taskSiteCrawlSync)
  .then(taskGenerateSpec)
  .commit()
