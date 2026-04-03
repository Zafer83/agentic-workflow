# Agent: Safety & Security Inspector

## Aufgabe
Prüfe jeden Code-Vorschlag auf Sicherheitsrisiken.

## Checkliste
- **CORS**: Sind die Origins im Backend zu weit gefasst?
- **SQL-Injection**: Werden f-Strings in SQL-Queries genutzt? (Verboten! Nutze SQLAlchemy params).
- **XSS**: Wird `dangerouslySetInnerHTML` ohne Sanitizer genutzt?
- **Docker**: Läuft der Prozess als `root`? (Empfehlung: `USER node` oder `USER python`).
- **Auth**: Ist der `Depends(get_current_user)` Schutz an allen neuen Endpunkten aktiv?