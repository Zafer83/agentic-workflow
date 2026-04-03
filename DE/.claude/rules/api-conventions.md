# Rule: API Conventions (RESTful Enterprise)

## Endpunkte & Methoden
- **Naming**: Plural-Nomen für Ressourcen (z.B. `/api/v1/users`).
- **Versionierung**: Immer Präfix `/api/v1/` nutzen.
- **Methoden**:
  - `GET`: Idempotent, keine Seiteneffekte.
  - `POST`: Ressource erstellen.
  - `PATCH`: Partielle Updates (bevorzugt gegenüber PUT).
  - `DELETE`: Ressource entfernen.

## Response-Struktur
Jede Antwort muss das Standard-Envelope nutzen:

```json
{
  "success": true,
  "data": {}, 
  "error": null,
  "meta": {
    "timestamp": "2026-04-03T15:00:00Z",
    "version": "v1"
  }
}