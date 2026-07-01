import { createStep } from '@mastra/core/workflows'

// Ad-hoc Task: task_token_limiter_demo
export const task_token_limiter_demo = createStep({
  id: 'task_token_limiter_demo',
  description: `Demonstrate TokenLimiter by having agent call read-file tool to produce a large response, then query the agent to show forgetting/pruning behavior.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: task_forgetful_interviewer_demo
export const task_forgetful_interviewer_demo = createStep({
  id: 'task_forgetful_interviewer_demo',
  description: `Interactive interviewer scenario where the agent may forget information that contains configured keywords (e.g., 'name').`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: task_technical_support_demo
export const task_technical_support_demo = createStep({
  id: 'task_technical_support_demo',
  description: `Support dialogue where user describes laptop overheating and agent uses web-search tool; memory TokenLimiter demonstrates retention/pruning.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
