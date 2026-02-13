from rdflib import Graph, Namespace, RDF
from rdflib.namespace import DCTERMS


def parse_kg(file_path: str):
    """
    Parse Knowledge Graph file (TTL/RDF) and extract ALL AgentO components.
    """
    # Namespaces
    AGENTO = Namespace("http://www.w3id.org/agentic-ai/onto#")
    DCT = DCTERMS

    # Load RDF Graph
    g = Graph()
    try:
        g.parse(file_path, format="turtle")
    except Exception as e:
        try:
            g.parse(file_path, format="xml")
        except:
            raise ValueError(f"Failed to parse RDF file. Please check TTL syntax in {file_path}. Error: {str(e)}")

    parsed = {
        "agents": [],
        "tasks": [],
        "tools": [],
        "goals": [],
        "workflows": [],
        "workflow_steps": [],
        "agent_interactions": [],
        "prompts": [],
        "teams": [],
    }

    # Build Task -> Agent mapping from NEW performedByAgent property
    # In new ontology: Task ---performedByAgent---> Agent
    task_to_agent = {}
    for task in g.subjects(RDF.type, AGENTO.Task):
        agent = g.value(task, AGENTO.performedByAgent)
        if agent:
            task_to_agent[str(task)] = str(agent)

    # Also check for Agent -> Task relationships (if ontology uses both directions)
    # Some implementations might still use hasTask or similar
    for agent in g.subjects(RDF.type, AGENTO.LLMAgent):
        # Check various possible task relationship properties
        for task_prop in [AGENTO.hasTask, AGENTO.performsTask]:
            for task in g.objects(agent, task_prop):
                task_id = str(task)
                if task_id not in task_to_agent:
                    task_to_agent[task_id] = str(agent)

    # Parse LLM Agents with all properties from new ontology
    for agent in g.subjects(RDF.type, AGENTO.LLMAgent):
        agent_id = str(agent)
        
        # Basic properties
        role = g.value(agent, AGENTO.agentRole)
        agent_id_prop = g.value(agent, AGENTO.agentID)
        title = g.value(agent, DCT.title)
        description = g.value(agent, DCT.description)
        
        # Goal reference - try specific property first, then general
        goal_ref = g.value(agent, AGENTO.hasAgentGoal) or g.value(agent, AGENTO.hasGoal)
        goal_label = None
        goal_desc = None
        if goal_ref:
            goal_label = g.value(goal_ref, DCT.title)
            goal_desc = g.value(goal_ref, DCT.description)
        
        # Tools - updated property name
        tools = []
        # Try new property name
        for tool in g.objects(agent, AGENTO.agentToolUsage):
            tools.append(str(tool))
        # Fallback to old property name if present
        if not tools:
            for tool in g.objects(agent, AGENTO.usesTool):
                tools.append(str(tool))
        
        # Agent interactions
        interacts_with = [str(o) for o in g.objects(agent, AGENTO.interactsWith)]
        
        # Language model
        language_model = g.value(agent, AGENTO.useLanguageModel)
        
        # Capabilities
        capabilities = [str(o) for o in g.objects(agent, AGENTO.hasAgentCapability)]
        
        # Configuration
        config = g.value(agent, AGENTO.hasAgentConfig)
        
        # Prompts
        agent_prompts = [str(o) for o in g.objects(agent, AGENTO.agentPrompt)]
        
        # Knowledge base
        knowledge = g.value(agent, AGENTO.hasKnowledge)
        
        # Operating environment
        environment = g.value(agent, AGENTO.operatesIn)
        
        parsed["agents"].append({
            "id": agent_id,
            "agent_id_prop": str(agent_id_prop) if agent_id_prop else "",
            "role": str(role) if role else "",
            "title": str(title) if title else "",
            "description": str(description) if description else "",
            "goal_title": str(goal_label) if goal_label else "",
            "goal_description": str(goal_desc) if goal_desc else "",
            "tools": tools,
            "interacts_with": interacts_with,
            "language_model": str(language_model) if language_model else "",
            "capabilities": capabilities,
            "config": str(config) if config else "",
            "prompts": agent_prompts,
            "knowledge": str(knowledge) if knowledge else "",
            "environment": str(environment) if environment else "",
        })
        
        # Track interactions
        for target in interacts_with:
            parsed["agent_interactions"].append({
                "from": agent_id,
                "to": target
            })

    # Parse Tasks with agent assignment from new ontology
    for task in g.subjects(RDF.type, AGENTO.Task):
        task_id = str(task)
        title = g.value(task, DCT.title)
        desc = g.value(task, DCT.description)
        
        # Expected output - check multiple possible properties
        expected = (g.value(task, AGENTO.expectedOutput) or 
                   g.value(task, AGENTO.taskExpectedOutput) or
                   g.value(task, AGENTO.taskOutputIndicator))
        
        # Get assigned agent from performedByAgent relationship
        assigned_agent = task_to_agent.get(task_id, "")
        
        # Task prompts
        task_prompts = [str(o) for o in g.objects(task, AGENTO.taskPrompt)]
        
        # Required capabilities
        required_caps = [str(o) for o in g.objects(task, AGENTO.requiresCapability)]
        
        # Required/produced resources
        required_resources = [str(o) for o in g.objects(task, AGENTO.requiresResource)]
        produced_resources = [str(o) for o in g.objects(task, AGENTO.producedResource)]
        
        # Contributing to objective
        objective = g.value(task, AGENTO.contributesToObjective)
        
        parsed["tasks"].append({
            "id": task_id,
            "title": str(title) if title else "",
            "description": str(desc) if desc else "",
            "expected_output": str(expected) if expected else "",
            "assigned_agent": assigned_agent,
            "prompts": task_prompts,
            "required_capabilities": required_caps,
            "required_resources": required_resources,
            "produced_resources": produced_resources,
            "objective": str(objective) if objective else "",
        })

    # Parse Tools
    for tool in g.subjects(RDF.type, AGENTO.Tool):
        tool_id = str(tool)
        title = g.value(tool, DCT.title)
        desc = g.value(tool, DCT.description)
        
        # Resources accessed by tool
        resources = [str(o) for o in g.objects(tool, AGENTO.resourceUsage)]
        
        # Tool capabilities
        capabilities = [str(o) for o in g.objects(tool, AGENTO.hasCapability)]
        
        # Tool configuration
        config = g.value(tool, AGENTO.hasToolConfig)
        
        # Tool using other tools
        tool_usage = [str(o) for o in g.objects(tool, AGENTO.toolUsage)]
        
        parsed["tools"].append({
            "id": tool_id,
            "title": str(title) if title else "",
            "description": str(desc) if desc else "",
            "resources": resources,
            "capabilities": capabilities,
            "config": str(config) if config else "",
            "tool_usage": tool_usage,
        })

    # Parse Goals
    for goal in g.subjects(RDF.type, AGENTO.Goal):
        title = g.value(goal, DCT.title)
        desc = g.value(goal, DCT.description)
        parsed["goals"].append({
            "id": str(goal),
            "title": str(title) if title else "",
            "description": str(desc) if desc else ""
        })

    # Parse Prompts
    for prompt in g.subjects(RDF.type, AGENTO.Prompt):
        prompt_id = str(prompt)
        context = g.value(prompt, AGENTO.promptContext)
        instruction = g.value(prompt, AGENTO.promptInstruction)
        input_data = g.value(prompt, AGENTO.promptInputData)
        output_indicator = g.value(prompt, AGENTO.promptOutputIndicator)
        
        parsed["prompts"].append({
            "id": prompt_id,
            "context": str(context) if context else "",
            "instruction": str(instruction) if instruction else "",
            "input_data": str(input_data) if input_data else "",
            "output_indicator": str(output_indicator) if output_indicator else "",
        })

    # Parse Teams (Crews in CrewAI terminology)
    for team in g.subjects(RDF.type, AGENTO.Team):
        team_id = str(team)
        title = g.value(team, DCT.title)
        desc = g.value(team, DCT.description)
        
        # Team members
        members = [str(o) for o in g.objects(team, AGENTO.hasAgentMember)]
        
        # Team goals
        team_goals = [str(o) for o in g.objects(team, AGENTO.hasTeamGoal)]
        
        # Team objectives
        objectives = [str(o) for o in g.objects(team, AGENTO.hasObjective)]
        
        # Workflow pattern
        workflow_pattern = g.value(team, AGENTO.hasWorkflowPattern)
        
        # System config
        config = g.value(team, AGENTO.hasSystemConfig)
        
        parsed["teams"].append({
            "id": team_id,
            "title": str(title) if title else "",
            "description": str(desc) if desc else "",
            "members": members,
            "goals": team_goals,
            "objectives": objectives,
            "workflow_pattern": str(workflow_pattern) if workflow_pattern else "",
            "config": str(config) if config else "",
        })

    # Parse WorkflowPatterns
    for wf in g.subjects(RDF.type, AGENTO.WorkflowPattern):
        title = g.value(wf, DCT.title)
        desc = g.value(wf, DCT.description)
        steps = [str(o) for o in g.objects(wf, AGENTO.hasWorkflowStep)]
        
        # Related patterns
        related = [str(o) for o in g.objects(wf, AGENTO.hasRelatedPattern)]
        sub_patterns = [str(o) for o in g.objects(wf, AGENTO.hasSubPattern)]
        next_pattern = g.value(wf, AGENTO.nextPattern)
        
        parsed["workflows"].append({
            "id": str(wf),
            "title": str(title) if title else "",
            "description": str(desc) if desc else "",
            "steps": steps,
            "related_patterns": related,
            "sub_patterns": sub_patterns,
            "next_pattern": str(next_pattern) if next_pattern else "",
        })

    # Parse WorkflowSteps (including StartStep and EndStep subclasses)
    # Collect all step instances - query for WorkflowStep, StartStep, and EndStep
    all_steps = set()
    for step in g.subjects(RDF.type, AGENTO.WorkflowStep):
        all_steps.add(step)
    for step in g.subjects(RDF.type, AGENTO.StartStep):
        all_steps.add(step)
    for step in g.subjects(RDF.type, AGENTO.EndStep):
        all_steps.add(step)
    
    for step in all_steps:
        step_id = str(step)
        title = g.value(step, DCT.title)
        desc = g.value(step, DCT.description)
        
        # Performed by (could be agent or tool)
        performed_by = g.value(step, AGENTO.performedBy)
        performed_by_agent = g.value(step, AGENTO.performedByAgent)
        
        # Step navigation
        next_step = g.value(step, AGENTO.nextStep)
        related_steps = [str(o) for o in g.objects(step, AGENTO.relatedStep)]
        step_order = g.value(step, AGENTO.stepOrder)
        
        # Associated task
        associated_task = g.value(step, AGENTO.hasAssociatedTask)
        
        # Step type
        is_start = (step, RDF.type, AGENTO.StartStep) in g
        is_end = (step, RDF.type, AGENTO.EndStep) in g
        
        parsed["workflow_steps"].append({
            "id": step_id,
            "title": str(title) if title else "",
            "description": str(desc) if desc else "",
            "performed_by": str(performed_by) if performed_by else "",
            "performed_by_agent": str(performed_by_agent) if performed_by_agent else "",
            "next_step": str(next_step) if next_step else "",
            "related_steps": related_steps,
            "step_order": int(step_order) if step_order else 0,
            "associated_task": str(associated_task) if associated_task else "",
            "is_start_step": is_start,
            "is_end_step": is_end,
        })

    print(f"[INFO] Parsed {len(parsed['agents'])} agents, "
          f"{len(parsed['tasks'])} tasks, {len(parsed['tools'])} tools, "
          f"{len(parsed['goals'])} goals, {len(parsed['prompts'])} prompts, "
          f"{len(parsed['teams'])} teams, "
          f"{len(parsed['workflows'])} workflows, {len(parsed['workflow_steps'])} steps, "
          f"{len(parsed['agent_interactions'])} interactions.")

    return parsed


# Quick test
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        example_path = sys.argv[1]
    else:
        example_path = "v2/kg/CrewAI/v2/kg/CrewAI/game-builder-crew_instances.ttl"
    
    try:
        result = parse_kg(example_path)
        print("\n=== Agents ===")
        for a in result["agents"]:
            print(f"ID: {a['id']}")
            print(f"  Role: {a['role']}")
            print(f"  Goal: {a['goal_title']}")
            print(f"  Tools: {len(a['tools'])}")
            print()
        
        print("\n=== Tasks ===")
        for t in result["tasks"]:
            print(f"ID: {t['id']}")
            print(f"  Description: {t['description'][:80]}..." if len(t['description']) > 80 else f"  Description: {t['description']}")
            print(f"  Assigned to: {t['assigned_agent']}")
            print()
            
        print("\n=== Teams ===")
        for team in result["teams"]:
            print(f"ID: {team['id']}")
            print(f"  Title: {team['title']}")
            print(f"  Members: {len(team['members'])}")
            print()
            
    except FileNotFoundError:
        print(f"[ERROR] RDF file not found: {example_path}")
        print("Please provide a valid RDF file path as argument or check the default path.")