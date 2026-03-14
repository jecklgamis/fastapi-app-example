GIT_COMMIT := $(shell git rev-parse --short HEAD)
DOCKER_IMAGE := fastapi-app-template:$(GIT_COMMIT)

.PHONY: all run dev install lint audit format test build-info docker-image docker-run docker-stop clean

all: clean install format lint test docker-image

install:
	uv pip install -e ".[dev]"
run:
	uvicorn app.main:app --host 0.0.0.0 --port 8080
dev:
	uvicorn app.main:app --reload --port 8080
lint:
	ruff check .
	mypy app/
audit:
	pip-audit
format:
	ruff check --fix .
	ruff format .
test:
	pytest -v
build-info:
	@echo '{"app":"fastapi-app-template","version":"0.1.0","git_commit":"$(GIT_COMMIT)","git_branch":"$(shell git rev-parse --abbrev-ref HEAD)","build_timestamp":"$(shell date -u +%Y-%m-%dT%H:%M:%SZ)"}' > build-info.json
docker-image: build-info
	docker build -t $(DOCKER_IMAGE) .
docker-run:
	-docker rm -f fastapi-app-template
	docker run --rm -d --name fastapi-app-template -p 8080:8080 $(DOCKER_IMAGE)
docker-stop:
	docker stop fastapi-app-template
clean:
	rm -rf .mypy_cache .pytest_cache .ruff_cache
	rm -rf *.egg-info dist build
	find . -type d -name __pycache__ -exec rm -rf {} +
