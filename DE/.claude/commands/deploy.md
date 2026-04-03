# Command: Deployment Pipeline

## 1. Build & Stage
- **Frontend**: `docker build -t frontend-prod -f frontend/Dockerfile.prod .`
- **Backend**: `docker build -t backend-prod -f backend/Dockerfile .`
- **Optimization**: Nutze Multi-Stage-Builds, um die Image-Größe < 200MB zu halten.

## 2. Pre-Flight Checks
- [ ] Alle Tests bestanden: `docker exec backend pytest`
- [ ] Security Scan: `trivy image backend-prod`
- [ ] DB Migrationen bereit: `alembic revision --autogenerate`

## 3. Rollout (Docker Compose / Swarm / K8s)
1. **Backup**: `docker exec db-container pg_dump > backup_$(date +%F).sql`
2. **Update**: `docker-compose -f docker-compose.prod.yml up -d --build`
3. **Migration**: `docker exec backend alembic upgrade head`

## 4. Post-Deployment
- Prüfe `/api/v1/health` auf Status 200.
- Überprufe Sentry/Logs auf unmittelbare Startfehler.