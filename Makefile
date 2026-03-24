install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/*.whl

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

lint:
	uv run ruff check gendiff

check: test lint