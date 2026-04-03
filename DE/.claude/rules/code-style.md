# Rule: Enterprise Code Style

## Python (Backend)
- **Formatting**: `ruff format` (Black-kompatibel).
- **Naming**: `snake_case` für Variablen/Funktionen, `PascalCase` für Klassen.
- **Typing**: Strikte Type-Hints für alle Funktionsparameter und Rückgabewerte.
- **Docstrings**: Google-Style für öffentliche APIs und komplexe Logik.

## TypeScript/React (Frontend)
- **Komponenten**: Functional Components mit `const Name: React.FC = () => { ... }`.
- **Hooks**: Eigene Hooks für API-Logik (`useFetchUsers`), kein `useEffect` direkt für Daten.
- **Tailwind**: Sortiere Klassen mit dem `prettier-plugin-tailwindcss`.
- **State**: Nutze `Zustand` oder `React Query` für Server-State.