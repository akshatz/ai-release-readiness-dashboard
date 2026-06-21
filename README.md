# AI Release Readiness Dashboard

An AI-powered dashboard that helps engineering teams determine whether a software release is ready for production.

The application aggregates release signals such as development completion, pull request status, staging deployments, QA validation, release notes, and production approvals to generate a release readiness score, identify blockers, and recommend next actions.

## Features

### Phase 1 - Release Command Center

* Release readiness scoring
* Risk assessment (Low, Medium, High)
* Release blockers detection
* Action recommendations
* REST API built with FastAPI
* Interactive API documentation with Swagger

### Phase 2 - AI Copilot (Upcoming)

* AI-generated release summaries
* AI risk prediction
* AI recommendations
* Conversational interface

Examples:

* Can we release today?
* What is blocking production?
* What should happen next?
* Which release step is risky?

## Tech Stack

### Backend

* Python 3.12+
* FastAPI
* Pydantic
* Uvicorn

### Frontend (Upcoming)

* React
* TypeScript
* Vite

### AI (Upcoming)

* OpenAI API

### Database (Upcoming)

* SQLite

## Project Structure

```text
release-readiness-dashboard/

backend/
├── app.py
├── database.py
├── models.py
├── schemas.py
├── routers/
│   └── release.py
└── services/
    ├── ai_service.py
    └── readiness_service.py

frontend/

requirements.txt

README.md
```

## Setup

### Create virtual environment

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
python3 -m pip install fastapi uvicorn sqlalchemy openai python-dotenv
```

## Run Backend

Navigate to backend:

```bash
cd backend
```

Start FastAPI:

```bash
uvicorn app:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Example API Request

POST `/release/readiness`

Request:

```json
{
  "release_name": "Buzz v2.8",
  "development_complete": true,
  "pr_merged": true,
  "staging_deployed": true,
  "qa_complete": false,
  "release_notes_created": false,
  "production_approval": false
}
```

Example response:

```json
{
  "release_name": "Buzz v2.8",
  "score": 55,
  "status": "NOT READY",
  "risk": "HIGH",
  "blockers": [
    "QA signoff pending",
    "Release notes missing",
    "Production approval pending"
  ],
  "recommendations": [
    "Complete QA validation",
    "Generate release notes",
    "Request production approval"
  ]
}
```

## Roadmap

### Phase 1

* [x] FastAPI backend
* [x] Release readiness scoring
* [x] Risk assessment
* [x] Blockers engine
* [x] Recommendations engine

### Phase 2

* [ ] React dashboard
* [ ] AI Copilot integration

### Phase 3

* [ ] Jira integration
* [ ] GitHub integration
* [ ] Deployment integration
* [ ] Historical release analytics

## Vision

Provide a single source of truth that answers one question:

> Is this release ready for production?
