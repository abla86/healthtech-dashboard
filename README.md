# HealthTech Dashboard

A full-stack demonstration project combining a FastAPI REST API with a responsive JavaScript monitoring dashboard.

The application uses simulated healthcare-technology device data and contains no patient or personal health information.

## Features

- FastAPI REST API
- Device monitoring dashboard
- API health endpoint
- Device status monitoring
- Battery metrics
- Responsive frontend
- CORS configuration
- Pydantic validation
- Create, read and delete API operations
- Interactive refresh
- Automatic dashboard metrics
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
