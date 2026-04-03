# Command: Troubleshooting & Debugging

## Connectivity Issues
- **Internal**: `docker exec backend curl http://frontend:3000` to check Docker DNS.
- **Port Conflict**: Check for processes blocking 8000/3000: `lsof -i :8000`.

## Container Failures
- **Logs**: `docker-compose logs -f [service_name]`
- **Exit Codes**: 
  - `137`: Out of Memory (check Docker resources).
  - `1`: Application Crash (check stack traces).

## Database Issues
- **Locking**: Check `pg_stat_activity` if migrations are hanging.
- **Reset**: `docker-compose down -v` (CAUTION: wipes all local data).