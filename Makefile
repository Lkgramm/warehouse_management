# === VARIABLES ===
PROJECT_NAME=warehouse-management
PYTHON_VERSION=3.11

# === DIRECTORIES & FILES ===
SRC_DIR=src
TEST_DIR=tests
PYTEST=poetry run pytest
BLACK=poetry run black
ISORT=poetry run isort
MYPY=poetry run mypy
FLAKE8=poetry run flake8

# === TARGETS ===

.PHONY: help
help:
	@echo "Available commands:"
	@echo "  install		Install project and dev dependencies"
	@echo "  dev			Install dev dependencies"
	@echo "  test			Run tests"
	@echo "  lint			Lint code with flake8"
	@echo "  format			Format code with black and isort"
	@echo "  typecheck		Check types with mypy"
	@echo "  clean			Remove __pycache__ and .pyc files"
	@echo "  run			Run main.py"
	@echo "  shell			Enter python shell in src directory"

install:
	poetry install

dev:
	poetry install --with dev

test:
	$(PYTEST) $(TEST_DIR) -v

lint:
	$(FLAKE8) $(SRC_DIR) $(TEST_DIR)

format:
	$(BLACK) $(SRC_DIR) $(TEST_DIR)
	$(ISORT) $(SRC_DIR) $(TEST_DIR)

typecheck:
	$(MYPY) $(SRC_DIR)

run:
	poetry run python $(SRC_DIR)/main.py

shell:
	cd $(SRC_DIR) && python

repl: shell

.DEFAULT_GOAL := help