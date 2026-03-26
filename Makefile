.PHONY: help setup run clean check-requirements

help:
	@echo "make setup - Create virtual environment and install dependencies"
	@echo "make run - Run the application"
	@echo "make clean - Clean temporary files"
	@echo "make check-requirements - Check that all imports are in requirements.txt"
	@echo "make typecheck - Run static type checking with mypy"

PYTHON = .venv/bin/python
PIP = .venv/bin/pip

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

MYPY = .venv/bin/mypy

typecheck:
	$(MYPY) src/ --config-file mypy.ini

BLACK = .venv/bin/black
FLAKE8 = .venv/bin/flake8

format:
	$(BLACK) src/ scripts/

lint:
	$(FLAKE8) src/ scripts/ --config pyproject.toml