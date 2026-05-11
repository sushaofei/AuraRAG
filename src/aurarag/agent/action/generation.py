"""RAG generation module.

Responsibilities:
- produce user-facing response from reasoning context
- keep output format stable for caller integration
"""

from __future__ import annotations


class RAGGenerator:
    """Action-layer generation boundary."""

    def generate(self, context: str) -> str:
        return f"Answer Draft:\n{context}"
