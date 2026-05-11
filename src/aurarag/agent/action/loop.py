"""Agent loop module.

Responsibilities:
- coordinate Perception -> Cognition -> Action flow
- determine when a single-step task can return final output
"""

from __future__ import annotations

from aurarag.agent.action.generation import RAGGenerator
from aurarag.agent.cognition.reasoning import RAGReasoner
from aurarag.agent.cognition.retrieval import RAGRetriever
from aurarag.agent.perception.ingestion import RAGIngestion


class AgentLoopController:
    """Main loop controller for one-turn pipeline execution."""

    def __init__(self) -> None:
        self.ingestion = RAGIngestion()
        self.retriever = RAGRetriever()
        self.reasoner = RAGReasoner()
        self.generator = RAGGenerator()

    def run_once(self, query: str, raw_text: str, source_type: str = "text") -> str:
        """Execute one simplified Perception -> Cognition -> Action cycle."""
        units = self.ingestion.ingest(raw_text=raw_text, source_type=source_type)
        evidence = self.retriever.retrieve(query=query, units=units)
        context = self.reasoner.build_context(query=query, evidence=evidence)
        return self.generator.generate(context=context)
