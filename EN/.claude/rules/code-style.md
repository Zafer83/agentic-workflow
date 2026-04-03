# Rule: Enterprise Code Style

## Python (Backend)
- **Tooling**: Use `ruff` for linting and formatting (Black-compatible).
- **Naming**: `snake_case` for variables/functions, `PascalCase` for classes.
- **Typing**: Mandatory Type-Hints for all function parameters and return values.
- **Documentation**: Use Google-Style docstrings for public APIs and complex logic.

## TypeScript/React (Frontend)
- **Components**: Functional Components preferred: `const MyComponent: React.FC = () => { ... }`.
- **Hooks**: Abstract API logic into custom hooks (`useUserData`), avoid raw `useEffect` for data fetching.
- **Styling**: Tailwind CSS classes must be sorted (use `prettier-plugin-tailwindcss`).
- **State**: Use `Zustand` for global state and `React Query` for server state.