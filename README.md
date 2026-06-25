# Ether LLC — Website

[日本語版](README.ja.md)

[Japanese README](README.md)

## What this project is

This repository hosts the Ether LLC organization website (`https://ether-llc.com`). It is a bilingual Japanese/English site served with Django template rendering on a Python Runtime (Vercel).

## Why it's useful

- Provides public organizational information in two languages from a single codebase: vision, company policy, business objectives, and legal pages (privacy / cookies).
- Manages both the corporate overview and product descriptions (e.g., GratefulMoments) in one repository.
- This README is one of the repo docs; additional metadata is in [`pyproject.toml`](pyproject.toml).

## Getting started (macOS)

Prerequisites:

- Python 3.12 or later (3.12 / 3.13 / 3.14 supported)
- `uv`

Setup:

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

Open `http://localhost:8000/` for the Japanese site and `http://localhost:8000/en/` for the English site.

## Local environment files

Real local environment files are private machine state and must not be committed.
Use the templates in `.envs/.local/*.example` when a local environment file is needed:

```bash
cp .envs/.local/.django.example .envs/.local/.django
cp .envs/.local/.postgres.example .envs/.local/.postgres
```

Replace placeholder values only in the untracked local copies. Vercel deployment secrets such as `DJANGO_SECRET_KEY` must be configured in Vercel or GitHub secret storage, not in this repository.

## Tests and help

- Smoke tests: [`tests/test_pages.py`](tests/test_pages.py)
- Run tests:

```bash
uv run pytest
```

- Lint / format:

```bash
uv run ruff check .            # Python
uv run djlint ether/templates/ # Django templates
uv run djlint ether/templates/ --reformat
```

For questions, check [`tests/test_pages.py`](tests/test_pages.py) and [`pyproject.toml`](pyproject.toml) for project configuration.

## Maintainers and contributing

Maintained by Ether LLC ([so.masuda.2003@ether-llc.com](mailto:so.masuda.2003@ether-llc.com))

This project is not open source. Confirm with maintainers before contributing.

## License

© 2026 Ether LLC. All rights reserved. This repository is published for reference only and is not licensed for reuse, modification, or redistribution. Contact the maintainers before using any part of it.
