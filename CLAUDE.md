# CLAUDE.md

## Project

FastAPI application template. Python 3.14+, async, no database. Docker via Python 3.14-slim.

## Structure

- `app/main.py` — FastAPI app entry point, registers routers
- `app/config.py` — Settings via pydantic-settings, env-specific configs (dev/test/prod)
- `app/routers/` — Route handlers: `root.py`, `probe.py`, `status.py`, `build_info.py`
- `tests/` — Async tests with pytest + httpx, shared fixture in `conftest.py`
- `Dockerfile` — Multi-stage build, Python 3.14-slim base, port 8080

## Commands

- `make install` — Install dependencies (`uv pip install -e ".[dev]"`)
- `make dev` — Start dev server with reload on port 8080
- `make run` — Start production server on port 8080
- `make format` — Auto-fix and format (`ruff check --fix .` + `ruff format .`)
- `make lint` — Lint and type-check (`ruff check .` + `mypy app/`)
- `make audit` — Dependency vulnerability scan (`pip-audit`)
- `make test` — Run tests (`pytest -v`)
- `make build-info` — Generate `build-info.json` with git commit, branch, timestamp
- `make docker-image` — Build Docker image (tagged with branch name)
- `make docker-run` — Run Docker container on port 8080
- `make docker-stop` — Stop Docker container
- `make up` — Build and run Docker container
- `make clean` — Remove caches and build artifacts
- `make all` — Full pipeline: clean, install, format, lint, test, docker-image

## Conventions

- Routers go in `app/routers/` and are registered in `app/main.py`
- Each router gets its own test file in `tests/test_<router>.py`
- Test client fixture is shared via `tests/conftest.py`
- Settings are added to `app/config.py` and the `.env.*` files (`.env.dev`, `.env.test`, `.env.prod`)
- `APP_ENV` environment variable selects the config: `dev` (default), `test`, `prod`
- Tests automatically set `APP_ENV=test` via `conftest.py`
- Port 8080 for all server commands
- `/status/` endpoint is protected with HTTP Basic Auth
