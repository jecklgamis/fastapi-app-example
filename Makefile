.PHONY: all run dev install lint format test image container clean

all: clean install format lint test image

install:
	uv pip install -e ".[dev]"
run:
	uvicorn app.main:app --host 0.0.0.0 --port 8080
dev:
	uvicorn app.main:app --reload --port 8080
lint:
	ruff check .
	mypy app/
format:
	ruff check --fix .
	ruff format .
test:
	pytest -v
image:
	docker build -t fastapi-app-template .
container:
	-docker rm -f fastapi-app-template
	docker run -d --name fastapi-app-template -p 8080:8080 fastapi-app-template
clean:
	rm -rf .mypy_cache .pytest_cache .ruff_cache
	rm -rf *.egg-info dist build
	find . -type d -name __pycache__ -exec rm -rf {} +
