# Agent Development Rules

## Principles

1. Build workflow agents, not simple chatbots.

2. Separate reasoning and execution.

LLM:
- understand
- plan
- decide

Tools:
- query data
- execute actions

3. Dangerous actions require human approval.

4. All important actions need audit logs.

## Code Rules

- modular design
- provider abstraction
- avoid vendor lock-in
- avoid hardcoded secrets

Every Agent should define:
- goal
- tools
- knowledge
- memory
- workflow
- permissions
