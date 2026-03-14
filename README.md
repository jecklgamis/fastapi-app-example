# fastapi-app-template

A production-ready FastAPI application template with Docker support.

## Tech Stack

- **FastAPI** - async web framework
- **Pydantic v2** - validation and settings management
- **Docker** - containerized deployment (Ubuntu 24.04 LTS)
- **Ruff** - linting and formatting
- **pytest** - testing with async support

## Project Structure

```
├── app/
│   ├── main.py            # FastAPI application entry point
│   ├── config.py           # Settings via pydantic-settings
│   └── routers/            # API route handlers
├── tests/                  # Test suite
├── Dockerfile
├── Makefile
└── pyproject.toml
```

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (recommended)

### Setup

```bash
# Clone the repository
git clone <repo-url> && cd fastapi-app-template

# Install dependencies
make install

# Copy environment variables
cp .env.example .env

# Start the dev server
make dev
```

The API will be available at `http://localhost:8080`.

### Using Docker

```bash
# Build the image
docker build -t fastapi-app-template .

# Run the container
docker run -d --name fastapi-app-template -p 8080:8080 fastapi-app-template

# Stop
docker stop fastapi-app-template && docker rm fastapi-app-template
```

## API Endpoints

| Method   | Endpoint          | Description                    |
|----------|-------------------|--------------------------------|
| `GET`    | `/`               | Welcome message                |
| `GET`    | `/health`         | Health check                   |
| `GET`    | `/probe/live`     | Liveness probe                 |
| `GET`    | `/probe/ready`    | Readiness probe                |
| `GET`    | `/probe/startup`  | Startup probe                  |
| `GET`    | `/status/`        | System status (Basic Auth)     |

Interactive API docs are available at `/docs` (Swagger UI) and `/redoc`.

## Development

```bash
# Run tests
make test

# Lint and type-check
make lint

# Auto-fix and format
make format
```

## Configuration

All settings are managed via environment variables (see `.env.example`):

| Variable                      | Default                     | Description                  |
|-------------------------------|-----------------------------|------------------------------|
| `APP_NAME`                    | `fastapi-app-template`      | Application name             |
| `DEBUG`                       | `false`                     | Enable debug mode            |
| `SECRET_KEY`                  | `change-me-in-production`   | Secret key for signing       |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `30`                        | Token expiry in minutes      |
| `STATUS_USERNAME`             | `admin`                     | Basic Auth username for /status |
| `STATUS_PASSWORD`             | `password`                  | Basic Auth password for /status |

## License

MIT
