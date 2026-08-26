# Portfolio Worklog

## 2026-08-26 — Documentation navigation

- Added a clear Start Here section linking scope, API documentation, local run instructions, source and the wider portfolio.
- Simplified the portfolio wording without changing implemented functionality.
- No application functionality was changed.

## 2026-08-26 — Baseline verification

- Added focused FastAPI API smoke/integration tests for health, listing, create/read/delete, validation and missing-device behaviour.
- Added GitHub Actions CI for Python compilation and the API test suite.
- Updated the README with the CI verification scope and explicit non-production status.

## 2026-08-26 — Frontend/API integration hardening

- Moved the frontend API base address out of JavaScript logic and into the page configuration (`data-api-base`).
- Added an explicit `/health` check before dashboard data is treated as available.
- Replaced `innerHTML` rendering of API-returned device values with DOM APIs and `textContent`.
- Preserved the existing dashboard features and API contract.
- Updated README documentation at the same time.

## Status

Demonstration project with automated backend baseline verification and hardened frontend/API integration. Clinical validation and production readiness are not claimed.
