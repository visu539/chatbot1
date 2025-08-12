# Backend (Django 5 + DRF)

Run locally:
- `python -m venv .venv && source .venv/bin/activate && pip install -r backend/requirements.txt`
- `python backend/manage.py migrate`
- `python backend/manage.py seed_demo_data`
- `python backend/manage.py runserver 0.0.0.0:8000`

Docs: `/api/docs/`

Key endpoints:
- Auth: `/api/auth/login/`, `/api/auth/refresh/`, `/api/auth/logout/`
- Users: `/api/users/me/`, `/api/users/me/profile/`
- CRM: `/api/clients/`, `/api/leads/`
- Portfolio: `/api/accounts/`, `/api/holdings/`, `/api/transactions/`, `/api/sips/`, `/api/clients/{id}/aum/`
- Proposals: `/api/proposals/`, `/api/proposals/{id}/export-pdf/`
- Documents: `/api/documents/`
- Dashboard: `/api/dashboard/summary/`, `/api/reports/aum-by-client/`