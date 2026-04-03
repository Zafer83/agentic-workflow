# Rule: Testing Standards

## Quality Gates
1. **Coverage**: Maintain a minimum of 80% code coverage for business logic.
2. **Backend**: Every new API endpoint requires an integration test in `tests/api/`.
3. **Frontend**: Critical UI interactions must be covered by `Vitest` or `Playwright`.

## Execution
- **Unit Tests**: `docker exec backend pytest -m "not integration"`
- **Integration**: `docker exec backend pytest -m integration` (requires running DB).
- **Optimization**: Use `--lf` (last failed) during development to iterate quickly.