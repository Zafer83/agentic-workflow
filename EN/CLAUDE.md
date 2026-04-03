# Project Guide: [Project Name]

## Tech Stack
- **Frontend**: React (Vite), TypeScript, Tailwind CSS.
- **Backend**: Python (FastAPI), SQLAlchemy, Pydantic.
- **Infrastruktur**: Docker & Docker Compose.

## Core Commands
- **Dev**: `docker-compose up --build`
- **Test Backend**: `docker exec backend pytest`
- **Test Frontend**: `cd frontend && npm test`
- **Linting**: `ruff check .` / `npm run lint`

## Architecture Principles
- Use the **Repository Pattern** for database access.
- Frontend: Dedicated **Service Layer** for all API communication.
- Backend: Strict **Type-Hints** and Pydantic models for all I/O.

## Agent Instructions
When starting a task, refer to the specialized agents in `.claude/agents/` for security and code quality guidelines.