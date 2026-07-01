import { createStep } from '@mastra/core/workflows'

// Ad-hoc Task: task_chatbot_reply_1
export const task_chatbot_reply_1 = createStep({
  id: 'task_chatbot_reply_1',
  description: `messages=[{"content": "Tell me a joke.", "role": "user"}]`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: task_chatbot_reply_2
export const task_chatbot_reply_2 = createStep({
  id: 'task_chatbot_reply_2',
  description: `messages=[{"content": "Repeat the joke.", "role": "user"}]`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
