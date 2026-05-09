# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the app

```bash
# Activate the project virtualenv first
source venv/bin/activate

# Run the dev server (port 5001, debug mode on)
/Users/pritam/Desktop/expense-tracker/venv/bin/python3 app.py
```

If port 5001 is already in use: `kill $(lsof -ti :5001)`

## Dependencies

```bash
pip install -r requirements.txt
```

Key packages: `flask`, `werkzeug`, `pytest`, `pytest-flask`.

## Project structure

This is a student learning project built step-by-step. Large parts are intentionally unimplemented — placeholder routes return plain strings and `database/db.py` is an empty stub.

- **`app.py`** — all Flask routes. Implemented: `/`, `/register`, `/login`, `/terms`, `/privacy`. Placeholder (students implement): `/logout`, `/profile`, `/expenses/add`, `/expenses/<id>/edit`, `/expenses/<id>/delete`.
- **`database/db.py`** — stub for `get_db()`, `init_db()`, `seed_db()` using SQLite. Students write this in Step 1.
- **`templates/base.html`** — shared layout: navbar (Sign in / Get started), footer with Terms and Privacy links.
- **`templates/landing.html`** — marketing landing page. Has a hero section with a YouTube modal (opens on "See how it works"). YouTube URL placeholder is in `data-src` on `#modalVideo`.
- **`static/css/style.css`** — single stylesheet for the entire project. Sections are clearly delimited with comment headers. Landing-page-specific styles (`.lp-*`) and modal styles live here alongside global styles.
- **`static/img/`** — dashboard-preview.png used as the modal image reference (currently replaced by YouTube embed).

## CSS conventions

All CSS variables are defined in `:root` in `style.css`. Use them (`--ink`, `--accent`, `--paper`, `--border`, etc.) rather than hardcoded colours. There is no build step — changes to `.css` or `.html` files are reflected immediately on page reload.

## Templates

All templates extend `base.html`. The `{% block head %}` override is available for page-specific CSS/JS but the project standard is to keep everything in `style.css`.
