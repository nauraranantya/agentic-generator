"""
Layer 2 – Pydantic Intermediate Representation (IR)

Strongly-typed data models that sit between SPARQL extraction (Layer 1)
and framework-specific file generation (Layer 3).

The primary IR is AgenticProject, which preserves agentO ontology concepts
and IRI-based relationships. Legacy framework-shaped models remain below as
adapter targets for the existing generators.
"""

from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field


# ──────────────────────────────────────────────
# Enums
# ──────────────────────────────────────────────

class ProcessType(str, Enum):
    """CrewAI Process type."""
    SEQUENTIAL = "sequential"
    HIERARCHICAL = "hierarchical"


class WorkflowType(str, Enum):
    """Framework-agnostic workflow topology inferred from agentO workflow data."""
    SEQUENTIAL = "sequential"
    PARALLEL = "parallel"
    BRANCHING = "branching"
    HIERARCHICAL = "hierarchical"
    LOOP = "loop"
    MIXED = "mixed"

# ──────────────────────────────────────────────
# Leaf Models
# ──────────────────────────────────────────────

class ConfigModel(BaseModel):
    """A single key-value configuration entry from KG :Config."""
    key: str = Field(..., description="Config key (e.g. 'role', 'api_key', 'process')")
    value: str = Field(..., description="Config value")


class LanguageModelModel(BaseModel):
    """Represents a KG :LanguageModel (LLM backing agents)."""
    iri: str = Field(..., description="Full IRI of the LanguageModel individual")
    name: str = Field("", description="Human-readable name / label")
    description: str = Field("", description="dcterms:description text")
    provider: str = Field("", description="Inferred provider (e.g. 'ollama', 'openai')")
    model_name: str = Field("", description="Model identifier (e.g. 'llama3.1', 'gpt-4o')")


class ToolConfigModel(BaseModel):
    """Tool-specific configuration entry."""
    key: str = Field(..., description="Config key (e.g. 'file_path', 'stock_name')")
    value: str = Field(..., description="Config value")


class ToolModel(BaseModel):
    """
    Represents a standalone KG :Tool (not LLMAgent).

    Maps to:
      - crew.py: tool import + instantiation at module level
      - agents.yaml: referenced in agent's tools list
    """
    iri: str = Field(..., description="Full IRI of the Tool individual")
    var_name: str = Field(..., description="Python variable name (snake_case)")
    label: str = Field("", description="rdfs:label or display name")
    class_name: str = Field("", description="Legacy inferred CrewAI tool class")
    description: str = Field("", description="Tool description")
    configs: List[ToolConfigModel] = Field(default_factory=list)
    capabilities: List[str] = Field(default_factory=list)


# ──────────────────────────────────────────────
# Agent Model
# ──────────────────────────────────────────────

class AgentModel(BaseModel):
    """
    Represents a KG :LLMAgent → CrewAI Agent.

    agents.yaml fields : role, goal, backstory
    crew.py fields     : tools, llm, allow_delegation, verbose
    """
    iri: str = Field(..., description="Full IRI")
    var_name: str = Field(..., description="Python method/variable name (snake_case)")
    agent_id: str = Field("", description=":agentID literal")

    # agents.yaml fields
    role: str = Field(..., description="Agent role")
    goal: str = Field(..., description="Agent goal")
    backstory: str = Field("", description="Legacy CrewAI backstory / system prompt")
    system_prompt: str = Field("", description="agentO Prompt context/instruction")
    interacts_with: List[str] = Field(

        default_factory=list
    )

    # crew.py fields
    tool_iris: List[str] = Field(default_factory=list, description="Tool IRI references")
    tool_var_names: List[str] = Field(default_factory=list, description="Legacy tool variable names")
    language_model: Optional[LanguageModelModel] = Field(None, description="Agnostic language model reference")
    llm: Optional[LanguageModelModel] = Field(None, description="Language model if not default")
    configs: Dict[str, str] = Field(default_factory=dict, description="All agent config key/value pairs")
    knowledge_iris: List[str] = Field(default_factory=list, description="Knowledge / memory IRI references")
    allow_delegation: Optional[bool] = Field(None, description="Allow delegation flag")
    verbose: Optional[bool] = Field(None, description="Verbose flag (None = not specified in KG → omit from output)")


# ──────────────────────────────────────────────
# Task Model
# ──────────────────────────────────────────────

class TaskModel(BaseModel):
    """
    Represents a KG :Task → CrewAI Task.

    tasks.yaml fields : description, expected_output
    crew.py fields    : agent, context, output_json, output_file
    """
    iri: str = Field(..., description="Full IRI")
    var_name: str = Field(..., description="Python method/variable name (snake_case)")
    label: str = Field("", description="rdfs:label")

    # tasks.yaml fields
    description: str = Field(..., description="Task description (may contain {placeholders})")
    expected_output: str = Field(..., description="Expected output description")
    prompt_instruction: str = Field("", description="agentO promptInstruction")
    prompt_input_data: str = Field("", description="agentO promptInputData")
    prompt_output_indicator: str = Field("", description="agentO promptOutputIndicator")
    prompt_context: str = Field("", description="agentO promptContext")

    # crew.py fields
    agent_iri: str = Field("", description="Agent IRI from :performedByAgent")
    agent_var_name: str = Field("", description="Assigned agent's var_name")
    context_task_var_names: List[str] = Field(
        default_factory=list,
        description="Prior task var_names this task depends on (requiresResource chain)"
    )
    output_json_model: Optional[str] = Field(
        None,
        description="Pydantic model name for structured JSON output"
    )
    produced_resources: List[str] = Field(default_factory=list)
    required_resources: List[str] = Field(default_factory=list)
    configs: Dict[str, str] = Field(default_factory=dict)


# ──────────────────────────────────────────────
# Workflow Step Model
# ──────────────────────────────────────────────

class WorkflowStepModel(BaseModel):
    """A single workflow step linking order → task."""
    iri: str = Field("", description="Full IRI of the WorkflowStep individual")
    var_name: str = Field("", description="Canonical step variable name")
    step_order: int = Field(..., description="Integer step order")
    task_iri: str = Field("", description="Associated task IRI")
    task_var_name: str = Field(..., description="Associated task var_name")
    step_type: str = Field("WorkflowStep", description="StartStep / WorkflowStep / EndStep")
    next_step_iris: List[str] = Field(default_factory=list, description="Outgoing :nextStep targets")
    agent_iri: str = Field("", description="Resolved agent IRI from associated task")
    description: str = Field("", description="Step description")


class WorkflowPatternModel(BaseModel):
    """agentO :WorkflowPattern with topology and step membership."""
    iri: str
    var_name: str
    label: str = ""
    description: str = ""
    steps: List[WorkflowStepModel] = Field(default_factory=list)
    workflow_type: WorkflowType = WorkflowType.SEQUENTIAL
    sub_pattern_iris: List[str] = Field(default_factory=list)


class MemoryModel(BaseModel):
    """agentO :Memory represented without framework-specific storage classes."""
    iri: str
    var_name: str
    label: str = ""
    description: str = ""
    configs: Dict[str, str] = Field(default_factory=dict)


# ──────────────────────────────────────────────
# Input Variable Model
# ──────────────────────────────────────────────

class InputVariableModel(BaseModel):
    """A template placeholder variable extracted from prompts."""
    name: str = Field(..., description="Variable name (e.g. 'company_domain')")
    default_value: str = Field("", description="Default value if found in KG")
    has_default: bool = Field(False, description="True if KG provides a concrete default value")
    alternative_values: List[str] = Field(
        default_factory=list,
        description="Other example values from KG (non-default KickoffInputBundle entries)",
    )


# ──────────────────────────────────────────────
# Top-level Crew Model
# ──────────────────────────────────────────────

class CrewProject(BaseModel):
    """
    Complete intermediate representation for one CrewAI project.

    This is the single data structure passed from Layer 1 → Layer 3.
    It contains all information needed to generate:
      - config/agents.yaml
      - config/tasks.yaml
      - crew.py
      - main.py
      - .env (optional)
    """
    # Metadata
    crew_name: str = Field(..., description="CamelCase crew class name (e.g. 'GameBuilderCrew')")
    crew_var_name: str = Field("", description="snake_case module name (e.g. 'game_builder_crew')")
    description: str = Field("", description="Team-level description")
    process: ProcessType = Field(ProcessType.SEQUENTIAL, description="Workflow process type")

    # Components
    agents: List[AgentModel] = Field(default_factory=list)
    tasks: List[TaskModel] = Field(default_factory=list)
    tools: List[ToolModel] = Field(default_factory=list)
    workflow_steps: List[WorkflowStepModel] = Field(default_factory=list)

    # Runtime
    input_variables: List[InputVariableModel] = Field(
        default_factory=list,
        description="Template variables for crew.kickoff(inputs={...})"
    )
    language_models: List[LanguageModelModel] = Field(default_factory=list)

    # Environment
    env_vars: List[ConfigModel] = Field(
        default_factory=list,
        description="Environment variables needed (API keys etc.)"
    )


class AgenticProject(BaseModel):
    """Framework-agnostic extraction result from a single KG file."""
    name: str
    var_name: str = ""
    description: str = ""
    agents: List[AgentModel] = Field(default_factory=list)
    tasks: List[TaskModel] = Field(default_factory=list)
    tools: List[ToolModel] = Field(default_factory=list)
    workflows: List[WorkflowPatternModel] = Field(default_factory=list)
    memories: List[MemoryModel] = Field(default_factory=list)
    language_models: List[LanguageModelModel] = Field(default_factory=list)
    input_variables: List[InputVariableModel] = Field(default_factory=list)
    env_vars: List[ConfigModel] = Field(default_factory=list)
    system_configs: Dict[str, str] = Field(default_factory=dict)


class AutoGenProject(BaseModel):
    """Adapter output for the AutoGen generator.

    Built by autogen.adapter.adapt() — consumed by autogen.generator.
    """
    name: str
    model_name: str = "gpt-4o-mini"
    team_type: str = "RoundRobinGroupChat"
    agents: List[AgentModel] = Field(default_factory=list)
    tasks: List[TaskModel] = Field(default_factory=list)
    tools: List[ToolModel] = Field(default_factory=list)
    ordered_tasks: List[TaskModel] = Field(default_factory=list)
    input_variables: List[InputVariableModel] = Field(default_factory=list)
    env_vars: List[ConfigModel] = Field(default_factory=list)


# ══════════════════════════════════════════════════════════════
# LangGraph IR Models
# (separate from CrewAI models above — different execution model)
# ══════════════════════════════════════════════════════════════

class LangGraphToolModel(BaseModel):
    """
    Represents a KG :Tool → LangGraph @tool stub.

    Maps to:
      - graph.py: @tool decorated function + tools_list
    """
    iri: str = Field(..., description="Full IRI of the Tool individual")
    var_name: str = Field(..., description="Python variable name (snake_case)")
    title: str = Field("", description="Human-readable tool title")
    description: str = Field("A tool", description="Tool description for the @tool docstring")


class LangGraphAgentModel(BaseModel):
    """
    Represents a KG :LLMAgent → LangGraph node function.

    Maps to:
      - graph.py: <var_name>_node() function
      - graph.py: StateGraph.add_node()
    """
    iri: str = Field(..., description="Full IRI of the LLMAgent individual")
    var_name: str = Field(..., description="Python variable/function name (snake_case)")
    role: str = Field("agent", description="Agent role (used as node description)")
    prompt: str = Field(
        "You are a helpful assistant.",
        description="System prompt injected as SystemMessage",
    )
    model_name: str = Field("gpt-4o-mini", description="LLM model identifier")
    tools_refs: List[str] = Field(
        default_factory=list,
        description="Tool IRI references assigned to this agent",
    )


class LangGraphNodeModel(BaseModel):
    """
    Represents a workflow step → LangGraph StateGraph node.

    Maps to:
      - graph.py: StateGraph.add_node(name, fn)
    """
    iri: str = Field(..., description="Full IRI of the WorkflowStep individual")
    name: str = Field(..., description="Node name (snake_case, used in add_node)")
    agent_ref: Optional[str] = Field(None, description="IRI of the agent assigned to this node")
    is_start: bool = Field(False, description="True if this is the START node")
    is_end: bool = Field(False, description="True if this is the END node")


class LangGraphEdgeModel(BaseModel):
    """
    Represents a directed edge between two graph nodes.

    Maps to:
      - graph.py: StateGraph.add_edge() or add_conditional_edges()
    """
    source: str = Field(..., description="Source node IRI or name")
    target: str = Field(..., description="Target node IRI or name")
    condition: Optional[str] = Field(None, description="Optional condition label for routing")


class LangGraphProject(BaseModel):
    """
    Complete intermediate representation for one LangGraph project.

    This is the single data structure passed from Layer 1 (extractor)
    to Layer 3 (generator).  It contains all information needed to
    generate:
      - graph.py          (the compiled StateGraph app)
      - main.py           (entry point)
      - config/inputs.yaml
      - .env.example
      - requirements.txt

    Mapping overview:
        KG :Tool          → LangGraphToolModel   → @tool stubs in graph.py
        KG :LLMAgent      → LangGraphAgentModel  → node functions in graph.py
        KG :WorkflowStep  → LangGraphNodeModel   → StateGraph.add_node()
        KG :nextStep      → LangGraphEdgeModel   → StateGraph.add_edge()
    """
    name: str = Field("LangGraph Project", description="Human-readable project name")
    tools: List[LangGraphToolModel] = Field(default_factory=list)
    agents: List[LangGraphAgentModel] = Field(default_factory=list)
    nodes: List[LangGraphNodeModel] = Field(default_factory=list)
    edges: List[LangGraphEdgeModel] = Field(default_factory=list)
    input_variables: List[InputVariableModel] = Field(
        default_factory=list,
        description="Runtime input variables (from agento-ext:KickoffInputBundle)",
    )

    @property
    def pattern_type(self) -> str:
        """
        Detect the graph execution pattern from the extracted IR.

          supervisor   – multiple LLM agents (router needed)
          tool_calling – single agent with at least one tool
          linear       – single agent, no tools
        """
        if len(self.agents) > 1:
            return "supervisor"
        if self.tools:
            return "tool_calling"
        return "linear"
