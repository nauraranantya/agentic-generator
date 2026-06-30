import { createStep } from '@mastra/core/workflows'

// Ad-hoc Task: Task: Get legal moves
export const task_get_legal_moves = createStep({
  id: 'task_get_legal_moves',
  description: `Call get_legal_moves() to obtain the legal moves in UCI format; parse or present the returned comma-separated list to decide on the next move.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
