/**
 * Agent: onboarding_topic_preference
 * ID: Onboarding Topic preference Agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

/**
 * onboarding_topic_preference
 * 
 * Instructions:
 * Collect customer's preferences on news topics.
 */
export const onboardingTopicPreferenceAgent = new Agent({
  id: `Onboarding Topic preference Agent`,
  name: `onboarding_topic_preference`,
  instructions: `Collect customer's preferences on news topics.`,
  model: 'openai/gpt-4o-mini',
})
