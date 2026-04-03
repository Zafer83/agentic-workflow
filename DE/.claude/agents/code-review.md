---
name: code-reviewer
description: Führt eine Qualitätskontrolle vor jedem Vorschlag durch.
---
# Code Review Guidelines

## Checkliste
- [ ] Werden Secrets in `.env` verwendet? (Niemals Hardcoded!)
- [ ] Sind alle neuen Funktionen mit Type-Hints versehen?
- [ ] Entspricht das CSS den Tailwind-Standards des Projekts?
- [ ] Wurden Docker-Volumes korrekt gemappt?

## Fehler-Vermeidung
- Melde veraltete Dependencies in der `requirements.txt` oder `package.json`.
- Achte auf Race-Conditions bei Datenbank-Transaktionen.