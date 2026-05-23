# Daily Open Picture

A tiny Python/Flask web app that shows today's date and one open licensed picture.

The pictures come from a curated Wikimedia Commons catalog of public domain images and rotate by date.

## Run locally with uv

```bash
uv sync
uv run python app.py
```

Open http://127.0.0.1:5000.

## Run locally with venv and pip

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Developer checks

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
pre-commit install
```

## What it does

- Picks one open/public-domain Wikimedia Commons image for the current date.
- Displays the date, picture, title, source link, author, and license.
- Keeps the UI simple and focused on one beautiful image per day.
