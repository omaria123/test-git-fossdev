.PHONY: help setup test clean

PYTHON = .venv/bin/python
PIP = .venv/bin/pip

help:
	@echo "Available commands:"
	@echo "make setup - Create virtual environment and install dependencies"
	@echo "make test  - Run tests"
	@echo "make clean - Clean virtual environment"

setup:
	python3 -m venv .venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install -e .

test:
	$(PYTHON) -m pytest tests/ -v

clean:
	rm -rf .venv
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete