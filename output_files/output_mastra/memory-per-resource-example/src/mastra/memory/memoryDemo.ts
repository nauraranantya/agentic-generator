/**
 * Memory: memoryDemo
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: libsql
 */

import { Memory } from '@mastra/memory'
import { LibSQLStore } from '@mastra/libsql'


export const memoryDemo = new Memory({
  storage: new LibSQLStore({
    id: 'mastra-libsql-store',
    url: 'file:./memory-demo.db',
  }),
  options: {
    lastMessages: 5,
    workingMemory: {
      enabled: true,
      scope: 'resource',
      template: `# User Profile
- **Name**: 
- **Location**: 
- **Interests**: 
- **Preferences**: 
- **Goals**: 
- **Important Notes**:`,
    },
  },
})
