# Rule: API Conventions (RESTful Enterprise)

## 1. Endpoints & Methods
- **Naming**: Use plural nouns for resources (e.g., `/api/v1/users`, `/api/v1/reports`).
- **Versioning**: All endpoints must be prefixed with `/api/v1/`.
- **HTTP Methods**:
  - `GET`: Retrieve a resource or collection. Must be idempotent.
  - `POST`: Create a new resource.
  - `PATCH`: Partial update of an existing resource (preferred over PUT).
  - `DELETE`: Remove a resource.

## 2. Standard Response Envelope
To ensure predictable parsing for the React frontend, every response must follow this JSON structure:

```json
{
  "success": true,
  "data": {}, 
  "error": null,
  "meta": {
    "timestamp": "2026-04-03T15:00:00Z",
    "version": "v1",
    "request_id": "uuid-string"
  }
}