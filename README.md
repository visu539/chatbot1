# Advisor MVP Monorepo

This is a PoC for a Financial Advisor/Distributor portal.

- Backend: Django 5 + DRF, PostgreSQL, JWT (SimpleJWT), DRF Spectacular, CORS, S3 (django-storages), SES (boto3)
- Frontend: Next.js 14 (App Router) + Tailwind CSS + React Query + Axios
- Deployment: AWS App Runner (backend), AWS Amplify (frontend), RDS PostgreSQL

## Structure

- `backend/` Django REST API
- `frontend/` Next.js app
- `.github/workflows/` CI pipelines

## Quickstart (Local)

1. Backend
   - Create `.env` from `backend/.env.example`
   - `python -m venv .venv && source .venv/bin/activate`
   - `pip install -r backend/requirements.txt`
   - `python backend/manage.py migrate`
   - `python backend/manage.py seed_demo_data`
   - `python backend/manage.py runserver 0.0.0.0:8000`

2. Frontend
   - Create `.env.local` from `frontend/.env.example`
   - `cd frontend && npm install && npm run dev`

Open API docs at `http://localhost:8000/api/docs/`

## Deployment

- Backend: Build Docker image and deploy to AWS App Runner. Provide env vars from `backend/.env.example`.
- Frontend: Connect repo to AWS Amplify, set env from `frontend/.env.example`, build with `npm run build`.

## Notes

- This PoC is production-ready in architecture but minimal in features.
- Replace AWS placeholders and verify SES/S3 permissions in your environment.
