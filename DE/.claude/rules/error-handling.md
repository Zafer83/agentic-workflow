# Regel: Fehlerbehandlung (Enterprise Error Handling)

## 1. Backend-Prinzipien (Python/FastAPI)
- **Keine Rohdaten-Exceptions**: Werfe niemals Standard-Exceptions direkt an den Client.
- **Globaler Handler**: Nutze eine Middleware/Exception-Handler, der alle Fehler in das Standard-Envelope-Format bringt.
- **Fehler-Klassen**: Definiere spezifische Fehlerklassen (z. B. `BusinessException`, `NotFoundException`).
- **Validierung**: Pydantic-Validierungsfehler müssen als 422 oder 400 mit einem `details`-Array zurückgegeben werden.

## 2. Frontend-Prinzipien (React)
- **Axios Interceptors**: Fange alle 4xx und 5xx Fehler zentral ab.
- **User-Feedback**: Zeige Fehlermeldungen über ein Toast-System oder Error-Boundaries an.
- **Logging**: Logge Fehler im Frontend (z. B. Sentry), aber zeige dem User nur bereinigte Nachrichten.

## 3. Format (JSON Envelope)
Jeder Fehler muss so aussehen:
```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "STR_CODE_Z_B_AUTH_FAILED",
    "message": "Benutzerlesbare Nachricht",
    "details": []
  }
}