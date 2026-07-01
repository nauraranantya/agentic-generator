/**
 * Workflow: onboarding_workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { onboardingPersonalInformationAgent, onboardingTopicPreferenceAgent, customerEngagementAgent } from '../agents'

// ── Workflow Steps ──

const taskOnboardingPersonalInfo = createStep({
  id: 'task_onboarding_personal_info',
  description: `Hello, I'm here to help you get started with our product. Could you tell me your name and location?`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Hello, I'm here to help you get started with our product. Could you tell me your name and location?
    // This step uses agent: onboardingPersonalInformationAgent
    // const result = await onboardingPersonalInformationAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_onboarding_personal_info not implemented yet')
  },
})

const taskOnboardingTopicPreference = createStep({
  id: 'task_onboarding_topic_preference',
  description: `Great! Could you tell me what topics you are interested in reading about?`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Great! Could you tell me what topics you are interested in reading about?
    // This step uses agent: onboardingTopicPreferenceAgent
    // const result = await onboardingTopicPreferenceAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_onboarding_topic_preference not implemented yet')
  },
})

const taskCustomerEngagementRequest = createStep({
  id: 'task_customer_engagement_request',
  description: `Let's find something fun to read.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Let's find something fun to read.
    // This step uses agent: customerEngagementAgent
    // const result = await customerEngagementAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('task_customer_engagement_request not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * onboarding_workflow
 */
export const onboardingWorkflow = createWorkflow({
  id: 'onboarding_workflow',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [taskOnboardingPersonalInfo, taskOnboardingTopicPreference, taskCustomerEngagementRequest],
})
  .then(taskOnboardingPersonalInfo)
  .then(taskOnboardingTopicPreference)
  .then(taskCustomerEngagementRequest)
  .commit()
