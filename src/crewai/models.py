from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field

from ..core.models import (
    AgentModel,
    CapabilityModel,
    ConfigModel,
    ConstraintModel,
    EnvironmentModel,
    GoalModel,
    HumanAgentModel,
    InputVariableModel,
    LanguageModelModel,
    ObjectiveModel,
    ProcessType,
    ResourceModel,
    TaskModel,
    ToolModel,
    WorkflowStepModel,
)


class CrewProject(BaseModel):
    """Framework-specific IR for CrewAI generation."""

    crew_name: str = Field(..., description="CamelCase crew class name (e.g. 'GameBuilderCrew')")
    crew_var_name: str = Field("", description="snake_case module name (e.g. 'game_builder_crew')")
    description: str = Field("", description="Team-level description")
    process: ProcessType = Field(ProcessType.SEQUENTIAL, description="Workflow process type")

    agents: List[AgentModel] = Field(default_factory=list)
    tasks: List[TaskModel] = Field(default_factory=list)
    tools: List[ToolModel] = Field(default_factory=list)
    workflow_steps: List[WorkflowStepModel] = Field(default_factory=list)

    input_variables: List[InputVariableModel] = Field(
        default_factory=list,
        description="Template variables for crew.kickoff(inputs={...})",
    )
    language_models: List[LanguageModelModel] = Field(default_factory=list)
    env_vars: List[ConfigModel] = Field(
        default_factory=list,
        description="Environment variables needed (API keys etc.)",
    )

    human_agents: List[HumanAgentModel] = Field(default_factory=list)
    goals: List[GoalModel] = Field(default_factory=list)
    objectives: List[ObjectiveModel] = Field(default_factory=list)
    capabilities: List[CapabilityModel] = Field(default_factory=list)
    environments: List[EnvironmentModel] = Field(default_factory=list)
    resources: List[ResourceModel] = Field(default_factory=list)
    constraints: List[ConstraintModel] = Field(default_factory=list)
