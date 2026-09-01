# Enterprise Agent Platform

A reusable enterprise AI Agent development platform.

Goals:
- Multi LLM provider support
- Tool calling
- Workflow orchestration
- RAG knowledge system
- MCP integration
- Human approval workflow

Target applications:
- Ecommerce Operation Agent
- PC Management Agent
- Enterprise Data Analyst Agent

## Development

Requirements:

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

Install dependencies and run the API:

```bash
uv sync
uv run uvicorn app.main:app --app-dir backend --reload
```

The API is available at `http://127.0.0.1:8000`, with health status at
`GET /health` and interactive documentation at `GET /docs`.

Run the verification suite:

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```
