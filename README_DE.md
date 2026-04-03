# 🚀 Enterprise Python-React Project (AI-Optimized)

Dieses Projekt ist ein hochmodernes Fullstack-Setup mit einem **FastAPI-Backend**, einem **React-Frontend** und einer vollautomatisierten **Docker-Infrastruktur**. 

Das Besondere: Es nutzt eine dedizierte `.claude` Struktur, um eine KI-gestützte Entwicklung (AI-Native Development) auf Enterprise-Niveau zu ermöglichen.

---

## 🏗 Projekt-Architektur

- **Backend:** Python 3.12, FastAPI (Asynchron), SQLAlchemy (ORM), Pydantic (Validierung).
- **Frontend:** React, Vite, TypeScript, Tailwind CSS.
- **Infrastruktur:** Docker & Docker Compose (PostgreSQL, Redis).
- **KI-Steuerung:** Agenten-basierte Workflows via `.claude/`.

---

## 🤖 Arbeiten mit Claude (KI-Befehle)

Dieses Repo ist darauf optimiert, dass Claude (oder andere KIs) genau weiß, was zu tun ist. Du kannst im Chat direkt folgende **Slash-Commands** nutzen:

### Zentrale Commands
* `/provision`: Initialisiert das gesamte Projekt (erstellt `.env`, startet Docker, führt Migrationen aus).
* `/init-repo`: Erstellt automatisch ein GitHub-Repository und pusht den aktuellen Stand.
* `/review`: Startet einen vollständigen Code-Check (Linting, Typen, Best Practices).
* `/deploy`: Bereitet das Production-Image vor und plant den Rollout.
* `/troubleshoot`: Analysiert Logs und Netzwerkverbindungen bei Fehlern.

---

## 📂 Die .claude Struktur erklärt

| Ordner | Inhalt | Nutzen |
| :--- | :--- | :--- |
| **agents/** | Rollen-Definitionen | Claude agiert als "Security Expert" oder "Senior Dev". |
| **rules/** | Projekt-Gesetze | Strikte Regeln für API-Design, Code-Style und Fehlerbehandlung. |
| **commands/** | Workflows | Schritt-für-Schritt Anleitungen für komplexe Terminal-Aufgaben. |
| **skills/** | Hilfs-Skripte | Python-Tools, die Claude helfen, Testberichte zu lesen. |

---

## 🛠 Schnellstart (Local Setup)

1.  **Voraussetzungen:**
    * Docker & Docker Compose installiert.
    * GitHub CLI (`gh`) installiert (für `/init-repo`).

2.  **Initialisierung:**
    Öffne den Claude-Chat (oder dein Terminal) und gib ein:
    ```bash
    # Über Claude:
    "Führe den /provision Command aus"
    
    # Manuell:
    cp .env.example .env
    docker-compose up -d
    ```

3.  **Entwicklung:**
    Die App ist erreichbar unter:
    - Frontend: `http://localhost:5173`
    - API-Docs: `http://localhost:8000/docs`

---

## 📏 Entwicklungs-Richtlinien (Rules)

Bitte halte dich (und weise Claude darauf hin) an die Regeln in `.claude/rules/`:
- **API:** Nutze immer das Standard-Envelope-Format für Antworten.
- **Errors:** Keine rohen Exceptions; nutze die Fehler-Codes aus `error-handling.md`.
- **Testing:** Jeder neue Feature-Zweig benötigt automatisierte Tests (Min. 80% Coverage).

---

## 📄 Lizenz
Privates Enterprise-Repository. Alle Rechte vorbehalten.