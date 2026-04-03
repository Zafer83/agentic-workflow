# Command: Troubleshooting Guide

## Problem: Container startet nicht
1. **Logs prüfen**: `docker-compose logs -f [service_name]`
2. **Exit Codes**: Prüfe auf `Exited (137)` (OOM Killer) oder `Exited (1)` (App-Fehler).
3. **Config**: `docker-compose config` prüfen, ob Envs korrekt geladen sind.

## Problem: API nicht erreichbar (Network)
1. **Internal Ping**: `docker exec backend curl frontend:3000` (Prüfe Docker-DNS).
2. **Ports**: `netstat -tulpen` – Belegt ein lokaler Prozess Port 8000 oder 3000?

## Problem: Datenbank-Lock / Migration Fail
1. **Alembic History**: `docker exec backend alembic history`.
2. **Force Unlock**: Falls Migrationen hängen, `alembic_version` Tabelle manuell prüfen.