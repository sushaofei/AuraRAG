# AuraRAG

An Agentic Retrieval-Augmented Generation (RAG) project.

## Project Structure

```text
AuraRAG/
├── .github/workflows/     # CI pipeline
├── docs/                  # Documentation
├── src/aurarag/           # Application source code
├── tests/                 # Test suite
├── LICENSE
├── README.md
└── pyproject.toml         # Project, formatter, linter, and test config
```

## Quick Start

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -e ".[dev]"
```

3. Run tests:

```bash
pytest
```

4. Run lint/format checks:

```bash
ruff check .
ruff format --check .
```
