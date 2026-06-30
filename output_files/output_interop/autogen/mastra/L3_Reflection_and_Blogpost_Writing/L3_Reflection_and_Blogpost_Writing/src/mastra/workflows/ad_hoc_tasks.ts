import { createStep } from '@mastra/core/workflows'

// Ad-hoc Task: SEO review task
export const seo_review_task = createStep({
  id: 'seo_review_task',
  description: `Review the following content. Return review into as JSON object only: {'Reviewer': '', 'Review': ''}. Here Reviewer should be your role.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Legal review task
export const legal_review_task = createStep({
  id: 'legal_review_task',
  description: `Review the following content. Return review into as JSON object only: {'Reviewer': '', 'Review': ''}.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
