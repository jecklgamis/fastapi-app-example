# CLAUDE.md

## Project

FastAPI application template. Python 3.12+, async, no database. Docker via Ubuntu 24.04 LTS.

## Structure

- `app/main.py` — FastAPI app entry point, registers routers
- `app/config.py` — Settings via pydantic-settings, loaded from `.env`
- `app/routers/` — Route handlers: `root.py`, `probe.py`, `status.py`
- `tests/` — Async tests with pytest + httpx, shared fixture in `conftest.py`
- `Dockerfile` — Ubuntu 24.04 LTS base, Python venv, port 8080

## Commands

- `make dev` — Start dev server with reload on port 8080
- `make run` — Start production server on port 8080
- `make test` — Run tests (`pytest -v`)
- `make lint` — Lint and type-check (`ruff check .` + `mypy app/`)
- `make format` — Auto-fix and format (`ruff check --fix .` + `ruff format .`)
- `make install` — Install dependencies (`uv pip install -e ".[dev]"`)
- `docker build -t fastapi-app-template .` — Build Docker image
- `docker run -d --name fastapi-app-template -p 8080:8080 fastapi-app-template` — Run container

## Conventions

- Routers go in `app/routers/` and are registered in `app/main.py`
- Each router gets its own test file in `tests/test_<router>.py`
- Test client fixture is shared via `tests/conftest.py`
- Settings are added to `app/config.py` and `.env.example`
- Port 8080 for all server commands
- `/status/` endpoint is protected with HTTP Basic Auth
