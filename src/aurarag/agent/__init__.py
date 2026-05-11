"""Agentic RAG architecture package.

This package defines a three-layer structure:
- Perception: ingest and normalize external knowledge.
- Cognition: retrieve and reason over evidence.
- Action: produce responses and control loop behavior.
"""

from .action.generation import RAGGenerator
from .action.loop import AgentLoopController
from .action.tool_use import ToolExecutor
from .cognition.reasoning import RAGReasoner
from .cognition.retrieval import RAGRetriever
from .perception.ingestion import RAGIngestion

__all__ = [
    "AgentLoopController",
    "RAGGenerator",
    "RAGIngestion",
    "RAGReasoner",
    "RAGRetriever",
    "ToolExecutor",
]
