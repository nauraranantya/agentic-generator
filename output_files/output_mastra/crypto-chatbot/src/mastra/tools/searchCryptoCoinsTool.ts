/**
 * Tool: Search crypto coins tool
 * 
 * Auto-generated from AgentO Knowledge Graph
 * 
 * Tool to search all available crypto coins by a keyword. Implements logic: fetch coin list from CoinGecko, try exact match by name (case-insensitive), if not found return first coin whose name contains the keyword.
 */

import { createTool } from '@mastra/core/tools'
import { z } from 'zod'

/**
 * Search crypto coins tool
 * 
 * Implementation: Tool to search all available crypto coins by a keyword. Implements logic: fetch coin list from CoinGecko, try exact match by name (case-insensitive), if not found return first coin whose name contains the keyword.
 */
export const searchCryptoCoinsTool = createTool({
  id: 'Search crypto coins tool',
  description: `Tool to search all available crypto coins by a keyword. Implements logic: fetch coin list from CoinGecko, try exact match by name (case-insensitive), if not found return first coin whose name contains the keyword.`,
  inputSchema: z.object({ keyword: z.string() }),
  outputSchema: z.object({example_fields: z.string()}),
  execute: async ({ inputData }) => {
    // TODO: Implement tool logic
    // 
    // Description: Tool to search all available crypto coins by a keyword. Implements logic: fetch coin list from CoinGecko, try exact match by name (case-insensitive), if not found return first coin whose name contains the keyword.
    // Configurations:
    //   - x-cg-demo-api-key (header): process.env.COINGECKO_API_KEY
    //   - endpoint: https://api.coingecko.com/api/v3/coins/list
    // 
    // Implementation should:
    // 1. Use inputData according to inputSchema
    // 2. Perform the tool's logic
    // 3. Return result matching outputSchema
    
    throw new Error('Tool Search crypto coins tool not implemented yet')
  },
})
