.PHONY: help setup run clean check-requirements typecheck format lint check

help:
	@echo "make setup - Create virtual environment and install dependencies"
	@echo "make run - Run the application"
	@echo "make clean - Clean temporary files"
	@echo "make check-requirements - Check that all imports are in requirements.txt"
	@echo "make typecheck - Run static type checking with mypy"
	@echo "make format - Auto-format code with black"
	@echo "make lint - Check code style with flake8"
	@echo "make check - Run all checks (typecheck + check-requirements + lint)"

PYTHON = .venv/bin/python
PIP = .venv/bin/pip
MYPY = .venv/bin/mypy
BLACK = .venv/bin/black
FLAKE8 = .venv/bin/flake8

setup:
	python3 -m venv .venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) src/app.py

clean:
	rm -rf .venv
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

check-requirements:
	$(PYTHON) scripts/check_requirements.py

typecheck:
	$(MYPY) src/ --config-file mypy.ini

format:
	$(BLACK) $(FILE)

lint:
	$(FLAKE8) src/ scripts/ --config pyproject.toml

check: typecheck check-requirements lint