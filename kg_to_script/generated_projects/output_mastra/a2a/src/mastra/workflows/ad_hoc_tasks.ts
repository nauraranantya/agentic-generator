import { createStep } from '@mastra/core/workflows'

// Ad-hoc Task: initial_query_task
export const initial_query_task = createStep({
  id: 'initial_query_task',
  description: `Task created by sending a message via the A2A client in src/index.ts. The code generates a messageId (message-\${Date.now}) and sends the 'query' prompt to the agent. Mastra's A2A implementation may return a Task object rather than a direct message; this behavior is noted but runtime details are not modeled beyond task semantics.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
