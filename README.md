# 🚀 Enterprise Python-React Project (AI-Optimized)

This project is a state-of-the-art full-stack setup featuring a **FastAPI backend**, a **React frontend**, and a fully automated **Docker infrastructure**. 

What makes it unique: It utilizes a dedicated `.claude` structure to enable enterprise-grade **AI-Native Development**.

---

## 🏗 Project Architecture

- **Backend:** Python 3.12, FastAPI (Asynchronous), SQLAlchemy (ORM), Pydantic (Validation).
- **Frontend:** React, Vite, TypeScript, Tailwind CSS.
- **Infrastructure:** Docker & Docker Compose (PostgreSQL, Redis).
- **AI Orchestration:** Agent-based workflows via `.claude/`.

---

## 🤖 Working with Claude (AI Commands)

This repository is optimized so that Claude (or other LLMs) knows exactly what to do. You can use the following **slash commands** directly in the chat:

### Core Commands
* `/provision`: Initializes the entire project (creates `.env`, starts Docker, runs migrations).
* `/init-repo`: Automatically creates a GitHub repository and pushes the current state.
* `/review`: Starts a full code check (linting, types, best practices).
* `/deploy`: Prepares the production image and plans the rollout.
* `/troubleshoot`: Analyzes logs and network connections in case of errors.

---

## 📂 The .claude Structure Explained

| Folder | Content | Purpose |
| :--- | :--- | :--- |
| **agents/** | Role Definitions | Claude acts as a "Security Expert" or "Senior Dev". |
| **rules/** | Project Laws | Strict rules for API design, code style, and error handling. |
| **commands/** | Workflows | Step-by-step instructions for complex terminal tasks. |
| **skills/** | Helper Scripts | Python tools that help Claude parse test reports. |

---

## 🛠 Quickstart (Local Setup)

1.  **Prerequisites:**
    * Docker & Docker Compose installed.
    * GitHub CLI (`gh`) installed (required for `/init-repo`).

2.  **Initialization:**
    Open the Claude chat (or your terminal) and enter:
    ```bash
    # Via Claude:
    "Execute the /provision command"
    
    # Manually:
    cp .env.example .env
    docker-compose up -d
    ```

3.  **Development:**
    The application is accessible at:
    - Frontend: `http://localhost:5173`
    - API Docs: `http://localhost:8000/docs`

---

## 📏 Development Guidelines (Rules)

Please adhere to (and remind Claude of) the rules located in `.claude/rules/`:
- **API:** Always use the standard envelope format for responses.
- **Errors:** No raw exceptions; use the error codes defined in `error-handling.md`.
- **Testing:** Every new feature branch requires automated tests (Min. 80% coverage).

---

## 📄 License
Private Enterprise Repository. All rights reserved.