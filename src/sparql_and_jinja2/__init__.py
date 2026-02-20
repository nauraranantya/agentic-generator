"""
Declarative Code Generation: SPARQL + Jinja2 pipeline.

Generates CrewAI code from AgentO Knowledge Graphs using
SPARQL queries for data extraction and Jinja2 templates for rendering.

Usage:
    python -m src.sparql_and_jinja2.run
"""

from .generator import generate_crewai

__all__ = ["generate_crewai"]
