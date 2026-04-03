---
name: testing-expert
description: Guidelines für Unit-, Integration- und E2E-Tests im Projekt.
---
# Testing Skill

## Backend (Python)
- Framework: `pytest`
- Mocks: Nutze `unittest.mock` oder `pytest-mock`.
- Alle API-Endpoints benötigen einen Integration-Test in `tests/api/`.

## Frontend (React)
- Framework: `Vitest` + `React Testing Library`.
- E2E: `Playwright`.

## Workflow
1. Vor jedem Feature-Commit: Führe relevante Tests aus.
2. Wenn Tests fehlschlagen: Analysiere den Traceback und fixen, bevor Code-Änderungen vorgeschlagen werden.