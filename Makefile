# Variables
SOURCE_DIR = investalchemy
TESTS_DIR = tests

# Default target
all: test format lint

# Run tests with coverage report
test:
	poetry run coverage run -m pytest $(TESTS_DIR)
	poetry run coverage report -m
	poetry run coverage html

# Format code using ruff
format:
	poetry run black $(SOURCE_DIR)
	poetry run ruff format $(SOURCE_DIR)

# Lint code using ruff
lint:
	poetry run ruff check $(SOURCE_DIR)

# Fix linting issues
fix:
	poetry run ruff check --fix $(SOURCE_DIR)

# Sort imports in the project
sort:
	poetry run ruff check --select I --fix $(SOURCE_DIR)

# Clean up generated files
clean:
	rm -rf .coverage htmlcov .pytest_cache .ruff_cache

.PHONY: all test format lint fix sort clean