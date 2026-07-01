/**
 * Workflow: text_utilities_workflow_pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow that defines the sequence of tasks for text capitalization and message formatting.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import tools used by workflow steps
import { capitalizeTool, formatMessagesTool } from '../tools'

// ── Workflow Steps ──

const capitalizeSentenceTask = createStep({
  id: 'capitalize_sentence_task',
  description: `Task: Capitalize the first letter of each word in a provided sentence-like string. Conceptual behavior: split input string on space characters, for each token convert the first character to uppercase and append the rest of the token unchanged, then join tokens using a single space to produce the output string.`,
  inputSchema: z.object({sentence: z.string()}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Instruction: Capitalize the first letter of each word in the input string. Implementation details: split the input on space characters; for each word, transform the first character to uppercase and keep the remaining characters unchanged; rejoin with single spaces. Input: a string representing a sentence. Output: a string where each word's first character is uppercase. Example: 'hello world' -> 'Hello World'.
    // This step uses tool: capitalizeTool
    // TODO: Implement step logic
    throw new Error('capitalize_sentence_task not implemented yet')
  },
})

const capitalizeTask = createStep({
  id: 'capitalize_task',
  description: `Task: Capitalize the first letter of a string (typically a single word). Conceptual behavior: take the string, replace its first character with its uppercase equivalent, and append the remaining substring unchanged.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Instruction: Capitalize the first character of the input string. Implementation details: if the string is non-empty, return Uppercase(firstChar) + remainder of string. Input: a string (often a single word). Output: the string with its first letter capitalized. Example: 'apple' -> 'Apple'.
    // This step uses tool: capitalizeTool
    // TODO: Implement step logic
    throw new Error('capitalize_task not implemented yet')
  },
})

const formatMessagesTask = createStep({
  id: 'format_messages_task',
  description: `Task: Serialize an array of BaseMessage objects into a single formatted string. Behavior summary: for each message in the array, determine its role by calling the message's getType() operation, obtain the message content; if content is a string, use it directly, otherwise serialize the content with JSON.stringify; then wrap the content in an XML-like tag using the role as the tag name and an index attribute, concatenating all formatted message blocks separated by newlines.`,
  inputSchema: z.object({}),
  outputSchema: z.object({XML: z.string()}),
  execute: async ({ inputData }) => {
    // Instruction: Given an ordered array of messages (BaseMessage[]), produce a single serialized string. For each message at index i: - obtain role via message.getType(); - obtain content: if content is a string, use it; otherwise convert content to a JSON string representation; - emit a block: '<{role} index="{i}'>\\n{contentString}\\n</{role}>' ; concatenate blocks with newlines between them. Input: an array of BaseMessage-like objects. Output: a single formatted string used for logging, transmission, or downstream processing.
    // This step uses tool: formatMessagesTool
    // TODO: Implement step logic
    throw new Error('format_messages_task not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * text_utilities_workflow_pattern
 *
 * Workflow that defines the sequence of tasks for text capitalization and message formatting.
 */
export const textUtilitiesWorkflowPattern = createWorkflow({
  id: 'text_utilities_workflow_pattern',
  inputSchema: z.object({sentence: z.string()}),
  outputSchema: z.object({XML: z.string()}),
  steps: [capitalizeSentenceTask, capitalizeTask, formatMessagesTask],
})
  .then(capitalizeSentenceTask)
  .then(capitalizeTask)
  .then(formatMessagesTask)
  .commit()
