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

## Features

- FastAPI REST API
- Device monitoring dashboard
- API health endpoint
- Device status and battery metrics
- Responsive frontend
- CORS configuration
- Pydantic validation
- Create, read and delete API operations
- Interactive refresh and dashboard metrics
- OpenAPI / Swagger documentation

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
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

## Data safety

Use simulated or non-sensitive demonstration data only. Do not commit patient or other personal health information to this public repository.

## Status

Demonstration / learning project. The README describes the functionality represented by the repository and does not claim clinical validation or production readiness.

## Portfolio

Part of the ABLA86 engineering portfolio. This repository contains the implementation and documentation for the project.
