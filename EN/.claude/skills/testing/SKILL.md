---
name: testing-expert
description: Guidelines for unit, integration, and E2E testing.
---
# Testing Skill

## Strategy
- **Unit**: Fast, isolated tests for pure functions.
- **Integration**: Testing API endpoints against a real (test) database.
- **E2E**: Testing critical user journeys (e.g., Login -> Dashboard).

## Execution Protocol
1. Before proposing a fix: Run failing tests to confirm the bug.
2. After implementing: Run the relevant test suite to ensure no regressions.
3. Use the `.claude/skills/testing/helpers.py` script to parse large JSON test reports for a concise summary.