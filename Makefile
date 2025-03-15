# Variables
POETRY = poetry
SOURCE_DIR = investalchemy
TESTS_DIR = tests

# Default target
all: test format lint

# Run tests with coverage report
test:
	$(POETRY) run coverage run -m pytest $(TESTS_DIR)
	$(POETRY) run coverage report -m
	$(POETRY) run coverage html

# Format code using ruff
format:
	$(POETRY) run black $(SOURCE_DIR)
	$(POETRY) run ruff format $(SOURCE_DIR)

# Lint code using ruff
lint:
	$(POETRY) run ruff check $(SOURCE_DIR)

# Fix linting issues
fix:
	$(POETRY) run ruff check --fix $(SOURCE_DIR)

# Sort imports in the project
sort:
	$(POETRY) run ruff check --select I --fix $(SOURCE_DIR)

# Clean up generated files
clean:
	rm -rf .coverage htmlcov .pytest_cache .ruff_cache

.PHONY: all test format lint fix sort clean