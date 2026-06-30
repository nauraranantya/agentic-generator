/**
 * Agent: LLM Agent
 * ID: chef-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - Moderation Processor: ModerationProcessor configuration:
      - model: openai('gpt-4.1-nano')
      - categories: ['hate','harassment','violence']
      - threshold: 0.7
      - strategy: 'block'
      - purpose: detect and block inappropriate content
    Modeled as a Capability used by agents as input processor.
 *   - PII Detector: PII detection processor used to redact or mask PII; modeled as a capability.
 *   - Prompt Injection Detector: A prompt injection detector that can block malicious instructions (modeled as capability).
 *   - testScorer (scorer1): A scorer named scorer1 that returns a constant score 1 in the source. Used by Mastra as a scoring primitive.
 *   - Answer Relevancy Scorer: Prebuilt answer relevancy scorer (createAnswerRelevancyScorer) using openai('gpt-4o'). Used by evalAgent.
 *   - PII Detector (configured): Configured with openai('gpt-4o') in source and used as an input processor to redact PII.
 *   - Prompt Injection Detector (configured): Configured with google gemini model in source; blocks prompt injection.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { cookingTool, weatherInfoTool } from '../tools'

// Import memory
import { chefAgentMemory } from '../memory'

/**
 * LLM Agent
 * 
 * Instructions:
 * Return a useful recipe given an ingredient and available tools/equipment.
 */
export const chefAgent = new Agent({
  id: `chef-agent`,
  name: `LLM Agent`,
  instructions: `Return a useful recipe given an ingredient and available tools/equipment.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    cookingTool,
    weatherInfoTool,
  },
  memory: chefAgentMemory,
})
