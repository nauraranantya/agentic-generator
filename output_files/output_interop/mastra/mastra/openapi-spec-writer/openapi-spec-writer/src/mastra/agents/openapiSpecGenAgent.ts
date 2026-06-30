/**
 * Agent: OpenAPI spec writer agent
 * ID: openapi-spec-gen-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - Convert markdown to OpenAPI spec: Extract endpoints, parameters, responses and models from markdown documentation and produce an OpenAPI fragment.
 *   - Merge OpenAPI fragments: Merge multiple OpenAPI fragments into a single valid OpenAPI spec (resolve conflicts, unify components).
 *   - Format spec as YAML: Produce a properly formatted YAML spec from textual content.
 */

import { Agent } from '@mastra/core/agent'

/**
 * OpenAPI spec writer agent
 * 
 * Instructions:
 * Produce a merged OpenAPI specification from website documentation and optionally open a PR with the spec in a repository.
 */
export const openapiSpecGenAgent = new Agent({
  id: `openapi-spec-gen-agent`,
  name: `OpenAPI spec writer agent`,
  instructions: `Produce a merged OpenAPI specification from website documentation and optionally open a PR with the spec in a repository.`,
  model: 'openai/gpt-3.5-turbo',
})
