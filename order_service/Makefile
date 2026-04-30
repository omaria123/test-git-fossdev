create-structure:
	mkdir src tests docs
	touch README.md setup.py requirements.txt
	touch docs/DOMAIN.md
	touch src/.gitkeep tests/.gitkeep

install-dep:
	pip install -r requirements.txt

install:
	pip install -e .

test-pytest:
	python3 -m pytest
test: install-dep install test-pytest

PORT ?= 8802
PRODUCT_SERVICE_URL ?= http://127.0.0.1:8001

install-poetry:
	poetry install

run:
	@echo "Starting Order Service on port $(PORT)..."
	@echo "Product Service URL: $(PRODUCT_SERVICE_URL)"
	PRODUCT_SERVICE_URL=$(PRODUCT_SERVICE_URL) \
	poetry run uvicorn src.app.main:app --host 127.0.0.1 --port $(PORT) --reload

clean:
	rm -rf .pytest_cache
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true