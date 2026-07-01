import { createStep } from '@mastra/core/workflows'

// Ad-hoc Task: init_first_chat_task
export const init_first_chat_task = createStep({
  id: 'init_first_chat_task',
  description: `Chat with user started now {timestamp}.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
