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

lint:
	uv run ruff check gendiff

check: test lint