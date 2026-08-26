# HealthTech Dashboard

A full-stack demonstration project combining a FastAPI REST API with a responsive JavaScript monitoring dashboard.

The application uses simulated healthcare-technology device data and contains no patient or personal health information.

## Start here

| Need | Go to |
|---|---|
| Understand the app | [Features](#features) |
| Understand the API | [API endpoints](#api-endpoints) |
| Run locally | [Run locally](#run-locally) |
| Inspect the source | [GitHub repository](https://github.com/abla86/healthtech-dashboard) |
| See the wider portfolio | [Developer portfolio](https://abla86.github.io/developer-portfolio/) |

## Verification

[![CI](https://github.com/abla86/healthtech-dashboard/actions/workflows/ci.yml/badge.svg)](https://github.com/abla86/healthtech-dashboard/actions/workflows/ci.yml)

The baseline CI compiles the Python backend and runs API smoke/integration checks covering health, device listing, create/read/delete behaviour, validation and missing-device handling.

## Features

- FastAPI REST API
- Device monitoring dashboard
- API health endpoint
- Device status and battery metrics
- Responsive frontend
- Configurable CORS policy
- Pydantic validation
- Create, read and delete API operations
- Interactive refresh and dashboard metrics
- OpenAPI / Swagger documentation
- Configurable frontend API endpoint
- Explicit API health check before dashboard data loading
- Safe text-based DOM rendering for returned device data
- Frontend request timeout and response-shape validation

## Technology Stack

### Backend

- Python
- FastAPI
- Pydantic
- Uvicorn
- REST API

### Frontend

- HTML5
- CSS3
- JavaScript
- Fetch API
- Responsive CSS

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API information |
| GET | `/health` | Health check |
| GET | `/devices` | List devices |
| GET | `/devices/{id}` | Get device |
| POST | `/devices` | Create device |
| DELETE | `/devices/{id}` | Delete device |

Interactive API documentation is available at `/docs` while the backend is running.

## Run Locally

Install backend dependencies:

```powershell
cd backend
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

Run the baseline tests:

```powershell
pip install pytest httpx
pytest -q
```

The frontend API endpoint is configured through the `<body data-api-base="...">` attribute in `frontend/index.html`. Change that value when the API is hosted somewhere other than the local development address.

### CORS configuration

Local browser origins on `localhost` and `127.0.0.1` are allowed automatically for development. For a hosted frontend, set `ALLOWED_ORIGINS` on the API as a comma-separated list of explicit origins, for example:

```text
ALLOWED_ORIGINS=https://example.example.com
```

The API does not enable credentialed cross-origin requests, and the documented HTTP methods remain limited to the API operations actually exposed by the application.

### Frontend API resilience

The dashboard gives each health/data request an 8-second timeout and validates the returned device payload before rendering. Invalid payloads are treated as an API failure instead of being rendered into the page.

## Data safety

Use simulated or non-sensitive demonstration data only. Do not commit patient or other personal health information to this public repository.

## Status

Demonstration / learning project with automated backend baseline verification. The frontend/API integration includes explicit health checking, configurable endpoint selection, safe DOM rendering, response validation, request timeouts and a configurable CORS policy. The README does not claim clinical validation or production readiness.

## Portfolio

Part of the ABLA86 engineering portfolio. This repository contains the implementation and documentation for the project.
