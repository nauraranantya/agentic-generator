/**
 * Agent: personal_information_collector
 * ID: onboarding_personal_information_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

/**
 * personal_information_collector
 * 
 * Instructions:
 * You are personal_information_collector.
 */
export const onboardingPersonalInformationAgent = new Agent({
  id: `onboarding_personal_information_agent`,
  name: `personal_information_collector`,
  instructions: `You are personal_information_collector.`,
  model: 'openai/gpt-3.5-turbo',
})
