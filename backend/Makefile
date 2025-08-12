install:
	python -m venv .venv && . .venv/bin/activate && pip install -r backend/requirements.txt

migrate:
	. .venv/bin/activate && python backend/manage.py migrate

seed:
	. .venv/bin/activate && python backend/manage.py seed_demo_data

run:
	. .venv/bin/activate && python backend/manage.py runserver 0.0.0.0:8000

collectstatic:
	. .venv/bin/activate && python backend/manage.py collectstatic --noinput