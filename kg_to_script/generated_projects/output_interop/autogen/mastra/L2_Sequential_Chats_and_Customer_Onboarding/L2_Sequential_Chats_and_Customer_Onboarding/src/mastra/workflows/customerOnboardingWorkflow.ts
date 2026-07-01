/**
 * Workflow: customer_onboarding_workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * A workflow pattern composed of three sequential chat steps to onboard a customer: (1) collect personal info, (2) collect topic preferences, (3) request engagement content.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// ── Workflow Steps ──

const taskCollectPersonalInfo = createStep({
  id: 'task_collect_personal_info',
  description: `sender: onboarding_personal_information_agent; recipient: customer_proxy_agent; summary_method: reflection_with_llm; summary_args: { 'summary_prompt': "Return the customer information into as JSON object only: {'name': '', 'location': ''}" }; max_turns: 2; clear_history: True`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Return the customer information into as JSON object only: {'name': '', 'location': ''}
    // TODO: Implement step logic
    throw new Error('task_collect_personal_info not implemented yet')
  },
})

const taskCollectTopicPreferences = createStep({
  id: 'task_collect_topic_preferences',
  description: `sender: onboarding_topic_preference_agent; recipient: customer_proxy_agent; summary_method: reflection_with_llm; max_turns: 1; clear_history: False`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Great! Could you tell me what topics you are interested in reading about?
    // TODO: Implement step logic
    throw new Error('task_collect_topic_preferences not implemented yet')
  },
})

const taskCustomerProxyToEngagement = createStep({
  id: 'task_customer_proxy_to_engagement',
  description: `sender: customer_proxy_agent; recipient: customer_engagement_agent; message: "Let's find something fun to read."; summary_method: reflection_with_llm; max_turns: 1`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Let's find something fun to read.
    // TODO: Implement step logic
    throw new Error('task_customer_proxy_to_engagement not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * customer_onboarding_workflow
 *
 * A workflow pattern composed of three sequential chat steps to onboard a customer: (1) collect personal info, (2) collect topic preferences, (3) request engagement content.
 */
export const customerOnboardingWorkflow = createWorkflow({
  id: 'customer_onboarding_workflow',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [taskCollectPersonalInfo, taskCollectTopicPreferences, taskCustomerProxyToEngagement],
})
  .then(taskCollectPersonalInfo)
  .then(taskCollectTopicPreferences)
  .then(taskCustomerProxyToEngagement)
  .commit()
