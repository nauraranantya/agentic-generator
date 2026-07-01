/**
 * Agent: annotation-driven writer
 * ID: writer-annotation-agent-uuid-1
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - create draft document: Tool capability: prepare a text document with title and description according to a schema.
 *   - document generation: Agent capability: generate textual document content based on user messages and prompts.
 *   - tool binding: Agent capability: bind schema-defined tools to model so model can produce tool calls.
 *   - streaming output: Agent can process streaming outputs (chunks) from the language model and concatenate them into messages.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { draftTextDocumentTool } from '../tools'

/**
 * annotation-driven writer
 * 
 * Instructions:
 * You are annotation-driven writer.
 */
export const writerAnnotationAgentUuid1 = new Agent({
  id: `writer-annotation-agent-uuid-1`,
  name: `annotation-driven writer`,
  instructions: `You are annotation-driven writer.`,
  model: 'anthropic/claude-3-5-sonnet-latest',
  tools: {
    draftTextDocumentTool,
  },
})
