"""RAG ingestion module.

Responsibilities:
- accept raw source payloads (pdf/web/markdown/text metadata wrapper)
- normalize and segment content into retrievable units
- attach metadata for downstream retrieval and reasoning
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class KnowledgeUnit:
    """A normalized retrievable unit produced by the perception layer."""

    content: str
    source_type: str


class RAGIngestion:
    """Perception-layer boundary for ingestion and preprocessing."""

    def ingest(self, raw_text: str, source_type: str = "text") -> list[KnowledgeUnit]:
        """Normalize raw text into basic knowledge units.

        This placeholder keeps scope minimal for issue #4 while exposing
        a stable interface for future chunking/vectorization.
        """
        text = raw_text.strip()
        if not text:
            return []
        return [KnowledgeUnit(content=text, source_type=source_type)]
