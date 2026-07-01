import { createStep } from '@mastra/core/workflows'

// Ad-hoc Task: chat_interaction_task
export const chat_interaction_task = createStep({
  id: 'chat_interaction_task',
  description: `Template representing an interactive chat turn processed in the main loop (in chat.ts). For each user input, the code calls agent.stream(answer, { threadId, resourceId }) and consumes the returned textStream. The streaming output is masked and decorated for display (think tags and spinner). This Task is performed by the ExampleAgent and consumes a UserInput resource and produces a TextResponse resource.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
