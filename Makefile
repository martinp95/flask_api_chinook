# Makefile for Chinook Flask API

# Python interpreter
PYTHON := python3

# Default target
.DEFAULT_GOAL := help

## Run the Flask application
run:
	$(PYTHON) -m app.run

## Run unit tests with pytest
test:
	pytest -v tests/

## Run coverage and output to terminal
coverage:
	pytest --cov=app --cov-report=term --cov-report=html --cov-report=xml tests/

## Clean temporary files
clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	find . -type f -name 'coverage.xml' -delete
	rm -rf htmlcov .pytest_cache .coverage

## Format using black
format:
	black app tests

## Up the docker
up:
	docker compose up --build -d

## Down the docker
down:
	docker compose down -v
## Show help
help:
	@echo "Usage:"
	@echo "  make run        - Run the Flask app"
	@echo "  make test       - Run all tests"
	@echo "  make coverage   - Run tests with coverage"
	@echo "  make clean      - Clean temporary files"
	@echo "  make format     - Auto-format code using black"
	@echo "  make up         - Up the docker container"
	@echo "  make down       - Down the docker container"
