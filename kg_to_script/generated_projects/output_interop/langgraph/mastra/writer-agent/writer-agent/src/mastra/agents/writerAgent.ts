/**
 * Agent: writer
 * ID: writer_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Creates an initial draft document (short title and short description) given title/description inputs.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolDraftTextDocument } from '../tools'

/**
 * writer
 * 
 * Instructions:
 * You are writer.
 */
export const writerAgent = new Agent({
  id: `writer_agent`,
  name: `writer`,
  instructions: `You are writer.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolDraftTextDocument,
  },
})
