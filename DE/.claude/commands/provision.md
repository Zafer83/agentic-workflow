# Command: Provisioning & Setup

## Lokale Initialisierung
1. **Environment**: `cp .env.example .env`
2. **Infrastructure**: `docker-compose up -d db redis`
3. **Database**: 
   - `docker exec backend alembic upgrade head`
   - `docker exec backend python -m app.seeds.initial_data` (Seed-Skript)
4. **Dependencies**:
   - Backend: `pip install -r requirements.txt` (für IDE/Linting lokal)
   - Frontend: `npm install`

## Bereinigung
- `docker-compose down -v` entfernt alle Volumes inklusive DB-Daten.