/**
 * Tool: collectContactInfo
 * 
 * Auto-generated from AgentO Knowledge Graph
 * 
 * Tool ID: collectContactInfo     Description: Collects user contact information through elicitation (interactive).     Input schema: { reason?: string }     Behavior:       - Calls MCP elicitation session to send a request with JSON schema (name, email, phone).       - Waits for user response via an elicitation handler. Interprets actions: accept/reject/cancel.       - Returns a string summarizing collection outcome or an error.     Elicitation requestedSchema (JSON):       {         type: 'object',         properties: {           name: { type: 'string', title: 'Full Name', description: 'Your full name' },           email: { type: 'string', title: 'Email Address', description: 'Your email address', format: 'email' },           phone: { type: 'string', title: 'Phone Number', description: 'Your phone number (optional)' }         },         required: ['name','email']       }
 */

import { createTool } from '@mastra/core/tools'
import { z } from 'zod'

/**
 * collectContactInfo
 * 
 * Implementation: Tool ID: collectContactInfo
 */
export const collectContactInfoTool = createTool({
  id: 'collectContactInfo',
  description: `Tool ID: collectContactInfo
    Description: Collects user contact information through elicitation (interactive).
    Input schema: { reason?: string }
    Behavior:
      - Calls MCP elicitation session to send a request with JSON schema (name, email, phone).
      - Waits for user response via an elicitation handler. Interprets actions: accept/reject/cancel.
      - Returns a string summarizing collection outcome or an error.
    Elicitation requestedSchema (JSON):
      {
        type: 'object',
        properties: {
          name: { type: 'string', title: 'Full Name', description: 'Your full name' },
          email: { type: 'string', title: 'Email Address', description: 'Your email address', format: 'email' },
          phone: { type: 'string', title: 'Phone Number', description: 'Your phone number (optional)' }
        },
        required: ['name','email']
      }`,
  inputSchema: z.object({ reason: z.string() }),
  outputSchema: z.object({}),  // TODO: Define output schema
  execute: async ({ inputData }) => {
    // TODO: Implement tool logic
    // 
    // Description: Tool ID: collectContactInfo
    // 
    // Implementation should:
    // 1. Use inputData according to inputSchema
    // 2. Perform the tool's logic
    // 3. Return result matching outputSchema
    
    throw new Error('Tool collectContactInfo not implemented yet')
  },
})
