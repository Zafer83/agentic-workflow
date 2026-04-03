# Projekt-Leitfaden: [Projektname]

## Tech-Stack
- **Frontend**: React (Vite), Tailwind CSS, TypeScript
- **Backend**: Python 3.12 (FastAPI), SQLAlchemy, Pydantic
- **Infrastruktur**: Docker & Docker Compose, Postgres

## Terminal-Befehle
- **Entwicklung**: `docker-compose up --build`
- **Backend Tests**: `docker exec -it backend pytest`
- **Frontend Tests**: `cd frontend && npm test`
- **Linting**: `ruff check .` (Python), `npm run lint` (React)

## Coding Standards
- **Python**: Nutze Type-Hints, Google-Style Docstrings, Ruff für Linting.
- **React**: Funktionale Komponenten, Hooks, 'lucide-react' für Icons.
- **API**: Immer Pydantic-Models für Request/Response nutzen.
- **Docker**: Halte Images klein (Multi-stage builds).

## Architektur-Prinzipien
- Backend folgt dem Repository-Pattern.
- Frontend nutzt dedizierte Service-Layer für API-Calls (kein `fetch` direkt in Komponenten).