/**
 * Agent: topic_preference_collector
 * ID: onboarding_topic_preference_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

/**
 * topic_preference_collector
 * 
 * Instructions:
 * You are topic_preference_collector.
 */
export const onboardingTopicPreferenceAgent = new Agent({
  id: `onboarding_topic_preference_agent`,
  name: `topic_preference_collector`,
  instructions: `You are topic_preference_collector.`,
  model: 'openai/gpt-3.5-turbo',
})
