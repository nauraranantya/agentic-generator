from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

from ..core.models import (
    CapabilityModel,
    ConstraintModel,
    EnvironmentModel,
    GoalModel,
    HumanAgentModel,
    InputVariableModel,
    ObjectiveModel,
    ResourceModel,
    TaskModel,
)


class LangGraphToolModel(BaseModel):
    """Represents a KG :Tool mapped to a LangGraph @tool stub."""

    iri: str = Field(..., description="Full IRI of the Tool individual")
    var_name: str = Field(..., description="Python variable name (snake_case)")
    title: str = Field("", description="Human-readable tool title")
    description: str = Field("A tool", description="Tool description for the @tool docstring")


class LangGraphAgentModel(BaseModel):
    """Represents a KG :LLMAgent mapped to a LangGraph node function."""

    iri: str = Field(..., description="Full IRI of the LLMAgent individual")
    var_name: str = Field(..., description="Python variable/function name (snake_case)")
    role: str = Field("agent", description="Agent role (used as node description)")
    prompt: str = Field("You are a helpful assistant.", description="System prompt injected as SystemMessage")
    model_name: str = Field("gpt-4o-mini", description="LLM model identifier")
    tools_refs: List[str] = Field(default_factory=list, description="Tool IRI references assigned to this agent")


class LangGraphNodeModel(BaseModel):
    """Represents a workflow step mapped to a LangGraph node."""

    iri: str = Field(..., description="Full IRI of the WorkflowStep individual")
    name: str = Field(..., description="Node name (snake_case, used in add_node)")
    agent_ref: Optional[str] = Field(None, description="IRI of the agent assigned to this node")
    is_start: bool = Field(False, description="True if this is the START node")
    is_end: bool = Field(False, description="True if this is the END node")


class LangGraphEdgeModel(BaseModel):
    """Represents a directed edge between two graph nodes."""

    source: str = Field(..., description="Source node IRI or name")
    target: str = Field(..., description="Target node IRI or name")
    condition: Optional[str] = Field(None, description="Optional condition label for routing")


class LangGraphProject(BaseModel):
    """Framework-specific IR for LangGraph generation."""

    name: str = Field("LangGraph Project", description="Human-readable project name")
    tools: List[LangGraphToolModel] = Field(default_factory=list)
    agents: List[LangGraphAgentModel] = Field(default_factory=list)
    nodes: List[LangGraphNodeModel] = Field(default_factory=list)
    edges: List[LangGraphEdgeModel] = Field(default_factory=list)
    input_variables: List[InputVariableModel] = Field(
        default_factory=list,
        description="Runtime input variables (from agento-ext:KickoffInputBundle)",
    )
    tasks: List[TaskModel] = Field(default_factory=list, description="Original tasks for human_input detection in templates")

    human_agents: List[HumanAgentModel] = Field(default_factory=list)
    goals: List[GoalModel] = Field(default_factory=list)
    objectives: List[ObjectiveModel] = Field(default_factory=list)
    capabilities: List[CapabilityModel] = Field(default_factory=list)
    environments: List[EnvironmentModel] = Field(default_factory=list)
    resources: List[ResourceModel] = Field(default_factory=list)
    constraints: List[ConstraintModel] = Field(default_factory=list)

    @property
    def pattern_type(self) -> str:
        if len(self.agents) > 1:
            return "supervisor"
        if self.tools:
            return "tool_calling"
        return "linear"
