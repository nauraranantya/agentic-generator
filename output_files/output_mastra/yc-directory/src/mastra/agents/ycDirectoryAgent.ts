/**
 * Agent: YC Directory Agent
 * ID: yc-directory-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : Objective representing the evaluation goal to measure the relevancy of ycAgent answers using an automatic scorer.
 *   - : Objective requiring the agent to answer questions about companies in the YC 2024 directory using only the dataset fields: name, longDescription, tags, industries, batch.
 * Capabilities:
 *   - : A scorer created by createAnswerRelevancyScorer used in tests: model 'openai/gpt-4o' with options scale:1 and uncertaintyWeight:0.3.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { ycDirectoryTool } from '../tools'

/**
 * YC Directory Agent
 * 
 * Instructions:
 * Used as agent-level instructions for ycDirectoryAgent (src/mastra/agents/index.ts).
 */
export const ycDirectoryAgent = new Agent({
  id: `yc-directory-agent`,
  name: `YC Directory Agent`,
  instructions: `Used as agent-level instructions for ycDirectoryAgent (src/mastra/agents/index.ts).`,
  model: 'anthropic/claude-3-5-sonnet-20241022',
  tools: {
    ycDirectoryTool,
  },
})
