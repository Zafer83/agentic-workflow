# Rule: Testing Requirements

## Quality Gates
1. **Backend**: Jeder neue API-Endpunkt benötigt einen Integration-Test in `tests/api/`.
2. **Frontend**: Komplexe UI-Logik benötigt Unit-Tests mit `Vitest`.
3. **Coverage**: Neue Features müssen die Gesamt-Coverage halten oder verbessern.

## Test-Execution
- **Unit**: `pytest -m "not integration"`
- **Integration**: `pytest -m integration` (erfordert laufende DB-Instanz).
- **Fast-Fail**: Claude sollte Tests mit `--lf` (last failed) starten, um Zeit zu sparen.