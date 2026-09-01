# System Architecture

## High Level

```
User
 |
Agent Runtime
 |
Workflow Engine
 |
Tools + Memory + Knowledge
 |
Enterprise Systems
```

## Agent Runtime

Responsible for:

- Reasoning loop
- Context management
- Tool selection
- Response generation

## Workflow Engine

Recommended technology:

- LangGraph

Responsibilities:

- State management
- Long running tasks
- Human approval
- Error recovery

## Provider Layer

Unified interface:

```
LLMProvider
 |
 +-- OpenAI
 +-- DeepSeek
 +-- Qwen
 +-- Claude
 +-- Ollama
```

## Tool Layer

Examples:

- Database tools
- Browser tools
- File tools
- ERP tools
- System tools

## Knowledge Layer

RAG provides:

- Company documents
- SOP
- Rules
- Manuals

## MCP Layer

Used for connecting external systems through standard protocols.
