# Command: System Provisioning & Setup

## Initial Environment
1. **Secrets**: `cp .env.example .env` (Update keys accordingly).
2. **Infra**: `docker-compose up -d db redis`
3. **Wait for DB**: Ensure Postgres is ready before migrating.

## Backend Setup
1. **Migrations**: `docker exec backend alembic upgrade head`
2. **Seeding**: `docker exec backend python -m app.seeds.initial_data`
3. **Local Tooling**: `pip install -r backend/requirements-dev.txt`

## Frontend Setup
1. **Install**: `cd frontend && npm install`
2. **Start**: `npm run dev`

## Cleanup / Reset
- Full Reset: `docker-compose down -v` (Deletes all volumes and data).