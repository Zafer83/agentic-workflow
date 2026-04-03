# Command: Review Workflow

## Schritte vor dem Push
1. **Linting**: `ruff check .` und `npm run lint`.
2. **Formatting**: `black .` und `prettier --write .`.
3. **Typing**: `mypy .` (Backend) und `tsc --noEmit` (Frontend).
4. **Security**: `bandit -r app/` (Python Security Check).

## Review-Kriterien
- Keine "Todo" Kommentare im Code.
- Keine `console.log` oder Python `print` Statements.
- Dokumentation von neuen Environment-Variablen in `.env.example`.