# Command: Deployment Pipeline

## 1. Build Phase
- **Frontend**: `docker build -t frontend-prod -f frontend/Dockerfile.prod .`
- **Backend**: `docker build -t backend-prod -f backend/Dockerfile .`

## 2. Pre-Flight Checks
- [ ] Run full test suite: `docker exec backend pytest`
- [ ] Run security scan: `trivy image backend-prod`
- [ ] Check migration status: `docker exec backend alembic current`

## 3. Rollout
1. **Database Backup**: `pg_dump -U user dbname > backup.sql`
2. **Update**: `docker-compose -f docker-compose.prod.yml up -d --build`
3. **Migrate**: `docker exec backend alembic upgrade head`

## 4. Verification
- Validate `/api/v1/health` returns status 200.
- Monitor logs for immediate runtime errors: `docker-compose logs -f`.