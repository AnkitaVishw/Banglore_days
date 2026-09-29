# Bangalore Days

A website for the first month in Bangalore. A newcomer creates an account, sets the locality they live in, and sees two lists for that locality only: **Settle in** (everyday needs) and **Explore** (places worth visiting).

This repository is a Django project at the repo root. It uses SQLite and Django templates. There is no separate frontend app.

## Layout

- `config/` — project settings, URLs, WSGI, and ASGI
- `accounts/` — registration, login, and the home locality on a user’s profile
- `places/` — localities, categories, shops, and favorites
- `templates/` — shared page layout
- `static/css/style.css` — shared styles
- `data/places.csv` — areas, categories, and places exported from the shared sheet

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

On macOS or Linux, activate the virtualenv with `source .venv/bin/activate`.

Open http://127.0.0.1:8000/ for the home page.
