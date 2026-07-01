import { createStep } from '@mastra/core/workflows'

// Ad-hoc Task: task_interactive_chat
export const task_interactive_chat = createStep({
  id: 'task_interactive_chat',
  description: `Represents the continuous interactive chat loop. Behavior: on start, an initial system message is sent (template varies depending on whether isFirstChat is true). Then user messages are read and the agent produces streaming responses. The agent uses memory.getThreadById to detect returning users and modifies the initial system prompt accordingly.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: task_agent_instantiation
export const task_agent_instantiation = createStep({
  id: 'task_agent_instantiation',
  description: `Describes Agent constructor parameters used in source: id='memory-agent', name='Memory Agent', instructions (see prompt_instructions), model=openai('gpt-4o-mini'), memory configured (memory_kb).`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
