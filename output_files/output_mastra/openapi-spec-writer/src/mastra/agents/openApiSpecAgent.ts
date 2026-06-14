/**
 * Agent: OpenAPI Spec Generator Agent
 * ID: openapi-spec-gen-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

/**
 * OpenAPI Spec Generator Agent
 * 
 * Instructions:
 * You are an expert Open API spec writer. You can take markdown documentation and extract all the information you can to generate an amazing Open API spec. You are also able to merge multiple fragmented Open API specs from the same source into a single compliant spec.
 */
export const openApiSpecAgent = new Agent({
  id: `openapi-spec-gen-agent`,
  name: `OpenAPI Spec Generator Agent`,
  instructions: `You are an expert Open API spec writer. You can take markdown documentation and extract all the information you can to generate an amazing Open API spec. You are also able to merge multiple fragmented Open API specs from the same source into a single compliant spec.`,
  model: 'openai/gpt-3.5-turbo',
})
