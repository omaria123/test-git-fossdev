.PHONY: help

help:
	@echo "make setup - Create virtual environment and install dependencies"
	@echo "make run - Run the application"
	@echo "make clean - Clean temporary files"

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