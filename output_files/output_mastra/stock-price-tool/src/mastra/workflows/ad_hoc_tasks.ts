import { createStep } from '@mastra/core/workflows'

// Ad-hoc Task: Example program invocation (src/index.ts)
export const index_ts = createStep({
  id: 'index_ts',
  description: `Sequence in source: const stockAgent = mastra.getAgent('stockAgent'); const response = await stockAgent.generate('What is the current stock price of Apple (AAPL)?'); The runtime inspects response.toolResults to find an entry where toolName === 'stockPrices' and reads result.currentPrice, then logs 'The current price of Apple (AAPL) is $<currentPrice>'.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
