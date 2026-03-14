# fastapi-app-template

[![Build](https://github.com/jecklgamis/fastapi-app-template/actions/workflows/build.yaml/badge.svg)](https://github.com/jecklgamis/fastapi-app-template/actions/workflows/build.yaml)

A production-ready FastAPI application template with Docker support.

Run from Docker Hub:
```bash 
docker run --rm --name fastapi-app-template -p 8080:8080 -it jecklgamis/fastapi-app-template:main
```

## Tech Stack

- **FastAPI** - async web framework
- **Pydantic v2** - validation and settings management
- **Docker** - containerized deployment (Python 3.14-slim)
- **Helm** - Kubernetes deployment chart
- **Ruff** - linting and formatting
- **pytest** - testing with async support

## Project Structure

```
├── app/
│   ├── main.py            # FastAPI application entry point
│   ├── config.py           # Environment-specific settings (dev/test/prod)
│   └── routers/            # API route handlers
├── tests/                  # Test suite
├── deployment/
│   └── k8s/helm/           # Helm chart and deploy Makefile
├── Dockerfile
├── Makefile
└── pyproject.toml
```

## Getting Started

### Prerequisites

- Python 3.14+
- [uv](https://github.com/astral-sh/uv) (recommended)
- [Docker](https://www.docker.com/) (for containerized deployment)

### Setup

```bash
# Clone the repository
git clone <repo-url> && cd fastapi-app-template

# Install dependencies
make install

# Start the dev server (uses .env.dev by default)
make dev
```

The API will be available at `http://localhost:8080`.

### Using Docker

```bash
# Build the image
docker build -t fastapi-app-template .

# Run the container
docker run --rm -d --name fastapi-app-template -p 8080:8080 fastapi-app-template

# Stop
docker stop fastapi-app-template
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

## Helm Chart

A Helm chart is provided in `deployment/k8s/helm/` for Kubernetes deployment.

```bash
cd deployment/k8s/helm

# Dry run to verify
make dry-run

# Install
make install

# Upgrade after changes
make upgrade

# Rollback
make rollback

# Uninstall
make uninstall
```

Default configuration in `chart/values.yaml`:

| Key                  | Default                                  |
|----------------------|------------------------------------------|
| `image.repository`   | `jecklgamis/fastapi-app-template`        |
| `image.tag`          | `main`                                   |
| `service.type`       | `ClusterIP`                              |
| `service.port`       | `80`                                     |
| `ingress.enabled`    | `true`                                   |
| `autoscaling.enabled`| `false`                                  |
| `replicaCount`       | `1`                                      |

## Configuration

Settings are managed via environment variables and loaded from env-specific files. Set `APP_ENV` to select the environment:

| Environment | Env File    | Debug | Description          |
|-------------|-------------|-------|----------------------|
| `dev`       | `.env.dev`  | `true`  | Local development (default) |
| `test`      | `.env.test` | `true`  | Test suite (set automatically) |
| `prod`      | `.env.prod` | `false` | Production           |

```bash
# Run with a specific environment
APP_ENV=prod make run
```

### Environment Variables

See `.env.example` for the full list:

| Variable                      | Default                     | Description                  |
|-------------------------------|-----------------------------|------------------------------|
| `APP_ENV`                     | `dev`                       | Environment (`dev`, `test`, `prod`) |
| `APP_NAME`                    | `fastapi-app-template`      | Application name             |
| `DEBUG`                       | `false`                     | Enable debug mode            |
| `STATUS_USERNAME`             | `admin`                     | Basic Auth username for /status |
| `STATUS_PASSWORD`             | `password`                  | Basic Auth password for /status |

## License

Apache 2.0 - see [LICENSE](LICENSE)
