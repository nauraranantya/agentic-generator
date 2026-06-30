import { createStep } from '@mastra/core/workflows'

// Ad-hoc Task: Chef initial recipe suggestion task
export const chef_initial_recipe_suggestion_task = createStep({
  id: 'chef_initial_recipe_suggestion_task',
  description: `In my kitchen I have: pasta, canned tomatoes, garlic, olive oil, and some dried herbs (basil and oregano). What can I make? Please keep your answer brief, only give me the high level steps.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Chef friend's ingredients recipe suggestion task
export const chef_friend_s_ingredients_recipe_suggestion_task = createStep({
  id: 'chef_friend_s_ingredients_recipe_suggestion_task',
  description: `Now I'm over at my friend's house, and they have: chicken thighs, coconut milk, sweet potatoes, and some curry powder.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Chef memory query task (asks what was cooked earlier)
export const chef_memory_query_task_asks_what_was_cooked_earlier = createStep({
  id: 'chef_memory_query_task_asks_what_was_cooked_earlier',
  description: `What did we cook before I went to my friends house?`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Chat initial system message task
export const chat_initial_system_message_task = createStep({
  id: 'chat_initial_system_message_task',
  description: `Chat with user started now \${new Date().toISOString()}. Don't mention this message. This means some time may have passed between this message and the one before. The user left and came back again. Say something to start the conversation up again.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Chat interactive loop task
export const chat_interactive_loop_task = createStep({
  id: 'chat_interactive_loop_task',
  description: ``,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
