# Agent Development Rules

## Principles

1. Build Agents, not simple chatbots.

Every feature should consider:

- Business goal
- Data source
- Tools
- Workflow

2. Separate reasoning and execution.

LLM:
- Understand
- Plan
- Decide

Tools:
- Query
- Execute

3. Critical actions require approval.

Never allow unrestricted AI execution.

## Engineering Rules

- Keep modules independent
- Avoid vendor lock-in
- Use interfaces
- Log important operations

## Every Agent Must Define

- Goal
- Available tools
- Memory strategy
- Workflow
- Permission model

## Security

Dangerous operations require:

Preview -> Approval -> Execute -> Audit
