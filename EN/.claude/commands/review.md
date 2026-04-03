# Command: Pull Request / Code Review Workflow

## Pre-Review Checks (Automation)
1. **Linting**: Run `ruff check` (Python) and `npm run lint` (React).
2. **Types**: Run `mypy` and `tsc --noEmit`.
3. **Testing**: Run full test suite via `docker exec backend pytest`.

## Manual Review Checklist
- [ ] No "TODO" or "FIXME" comments left in code.
- [ ] No `console.log` or Python `print` statements.
- [ ] New Environment Variables are documented in `.env.example`.
- [ ] Documentation (Docstrings/README) is updated.