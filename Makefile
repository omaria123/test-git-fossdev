.PHONY: help setup test clean build publish-test

PYTHON = .venv/bin/python
PIP = .venv/bin/pip

help:
	@echo "Available commands:"
	@echo "make setup        - Create virtual environment and install dependencies"
	@echo "make test         - Run tests"
	@echo "make build        - Build package (sdist + wheel)"
	@echo "make publish-test - Publish to TestPyPI"
	@echo "make clean        - Clean virtual environment and build artifacts"

setup:
	python3 -m venv .venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install -e .

test:
	$(PYTHON) -m pytest tests/ -v

build:
	$(PYTHON) -m pip install build
	$(PYTHON) -m build

publish-test:
	$(PYTHON) -m pip install twine
	$(PYTHON) -m twine upload --repository testpypi dist/*

clean:
	rm -rf .venv
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete