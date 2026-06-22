"""
Auto-generated LangGraph App: MyCrew

Pattern : Tool-Calling (single agent with tools)
Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - Build a Todo App: 
Human Agents:
  - human_user ()
Environments:
  - Development environment (development (file system, browser localStorage, UI)): 
Capabilities:
  - planning: Generate and maintain plan lists (executed, rejected, remaining) and choose next plan item.
  - file update: Prepare file content updates based on plan items and perform write actions (via a tool).
  - UI interaction / propose changes: Push UI items to present proposed changes to a human and capture approvals or rejections.
Resources:
  - step-1: scaffold commands: ```bash
npx create-react-app todo-app --template typescript
cd todo-app
mkdir -p src/{components,styles,utils}
```
  - step-2: TodoItem component: ```tsx
// src/components/TodoItem.tsx
import React from 'react';
import styles from '../styles/TodoItem.module.css';

interface TodoItemProps {
  id: string;
  text: string;
  completed: boolean;
  onToggle: (id: string) => void;
  onDelete: (id: string) => void;
}

export const TodoItem: React.FC<TodoItemProps> = ({ id, text, completed, onToggle, onDelete }) => (
  <div className={styles.todoItem}>
    <input type='checkbox' checked={completed} onChange={() => onToggle(id)} />
    <span className={completed ? styles.completed : ''}>{text}</span>
    <button onClick={() => onDelete(id)}>Delete</button>
  </div>
);
```
  - step-3: TodoContext (state management): ```tsx
// src/context/TodoContext.tsx
import React, { createContext, useContext, useReducer } from 'react';

type Todo = { id: string; text: string; completed: boolean; };

type TodoState = { todos: Todo[]; };
type TodoAction = 
  | { type: 'ADD_TODO'; payload: string }
  | { type: 'TOGGLE_TODO'; payload: string }
  | { type: 'DELETE_TODO'; payload: string };

const TodoContext = createContext<{
  state: TodoState;
  dispatch: React.Dispatch<TodoAction>;
} | undefined>(undefined);

export const TodoProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [state, dispatch] = useReducer(todoReducer, { todos: [] });
  return <TodoContext.Provider value={{ state, dispatch }}>{children}</TodoContext.Provider>;
};
```
  - step-4: AddTodo component (form and validation): ```tsx
// src/components/AddTodo.tsx
import React, { useState } from 'react';
import styles from '../styles/AddTodo.module.css';

export const AddTodo: React.FC<{ onAdd: (text: string) => void }> = ({ onAdd }) => {
  const [text, setText] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!text.trim()) {
      setError('Todo text cannot be empty');
      return;
    }
    onAdd(text.trim());
    setText('');
    setError('');
  };

  return (
    <form onSubmit={handleSubmit} className={styles.form}>
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder='Add a new todo'
      />
      {error && <div className={styles.error}>{error}</div>}
      <button type='submit'>Add Todo</button>
    </form>
  );
};
```
  - step-5: Filters and sorting: ```tsx
// src/components/TodoFilters.tsx
import React from 'react';

type FilterType = 'all' | 'active' | 'completed';

export const TodoFilters: React.FC<{
  currentFilter: FilterType;
  onFilterChange: (filter: FilterType) => void;
  onSortChange: (ascending: boolean) => void;
}> = ({ currentFilter, onFilterChange, onSortChange }) => (
  <div>
    <select value={currentFilter} onChange={(e) => onFilterChange(e.target.value as FilterType)}>
      <option value='all'>All</option>
      <option value='active'>Active</option>
      <option value='completed'>Completed</option>
    </select>
    <button onClick={() => onSortChange(true)}>Sort A-Z</button>
    <button onClick={() => onSortChange(false)}>Sort Z-A</button>
  </div>
);
```
  - step-6: local storage utils: ```tsx
// src/utils/storage.ts
const STORAGE_KEY = 'todos';

export const saveTodos = (todos: Todo[]) => {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(todos));
};

export const loadTodos = (): Todo[] => {
  const stored = localStorage.getItem(STORAGE_KEY);
  return stored ? JSON.parse(stored) : [];
};
```
  - Plan artifact (structured plan tool_call args snapshot): A JSON snapshot representing the tool_call args returned by the planner:
{
  "executedPlans": [...],
  "rejectedPlans": [...],
  "remainingPlans": [...]
}
This artifact is updated each planner run; initial remainingPlans is the canonical PLAN stored in PlanPrompt.promptInputData.
  - Plan input resource: Represents inputs consumed by the planner (previous tool_call responses, user approvals). Structured content is stored in PlanPrompt.promptInputData as JSON.
  - Simulated ToolMessage: User Approved Plan: The planner constructs a ToolMessage whose content is 'User has approved the plan.' to represent that the user accepted the plan and the workflow may proceed.
"""

import os
from typing import Annotated, TypedDict
from pathlib import Path
from dotenv import load_dotenv

_HERE = Path(__file__).parent
load_dotenv(_HERE / ".env", override=True)

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langchain_core.tools import tool

LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-4o-mini")


# ===========================================================
# Tool Stubs
# ===========================================================

@tool
def tool_plan(query: str) -> str:
    """Represents the logical tool 'plan' that is invoked by the planner node to expose executed/rejected/remaining plan lists as tool_call args."""
    # TODO: implement tool_plan
    return f"Stub result from 'tool_plan' for query: {query}"

@tool
def tool_update_file(query: str) -> str:
    """A tool"""
    # TODO: implement tool_update_file
    return f"Stub result from 'tool_update_file' for query: {query}"

tools_list = [tool_plan, tool_update_file]


# ===========================================================
# State
# ===========================================================

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]


# ===========================================================
# LLM
# ===========================================================

llm = ChatOpenAI(model=LLM_MODEL)
llm_with_tools = llm.bind_tools(tools_list)


# ===========================================================
# Agent Node
# ===========================================================

def open_code_agent_001_node(state: AgentState) -> dict:
    """planner-executor LLM agent (coordinates planning and performs file updates via tools and UI prompts) — invokes tools as needed and returns a response."""
    sys_msg = SystemMessage(content="""You are a planner-executor LLM agent (coordinates planning and performs file updates via tools and UI prompts).""")
    messages = [sys_msg] + state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}


# ===========================================================
# Graph
# ===========================================================

workflow = StateGraph(AgentState)
workflow.add_node("agent", open_code_agent_001_node)
workflow.add_node("tools", ToolNode(tools_list))

workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", tools_condition)
workflow.add_edge("tools", "agent")

app = workflow.compile(
    interrupt_before=["open_code_agent_001", "open_code_agent_001"]
)
