/**
 * Agent: onboarding_personal_information
 * ID: Onboarding Personal Information Agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

/**
 * onboarding_personal_information
 * 
 * Instructions:
 * Gather customer's name and location.
 */
export const onboardingPersonalInformationAgent = new Agent({
  id: `Onboarding Personal Information Agent`,
  name: `onboarding_personal_information`,
  instructions: `Gather customer's name and location.`,
  model: 'openai/gpt-4o-mini',
})
