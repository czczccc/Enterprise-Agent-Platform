# Architecture

## Overview

```
User
 |
Agent Runtime
 |
Workflow Engine (LangGraph)
 |
Tools / RAG / Memory / MCP
 |
Enterprise Systems
```

## Layers

### Provider Layer
Unified interface for:
- OpenAI
- DeepSeek
- Qwen
- Claude
- Ollama

### Agent Runtime
Responsible for:
- reasoning loop
- context management
- tool selection

### Tool Layer
Examples:
- database tools
- browser tools
- filesystem tools
- ERP APIs

### Knowledge Layer
RAG for:
- SOP documents
- company rules
- manuals

### Workflow Layer
LangGraph manages:
- state
- checkpoints
- human approval
- long running tasks
