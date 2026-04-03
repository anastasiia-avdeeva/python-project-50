import json
from typing import Any

import yaml


def get_file_extension(file_path: str) -> str:
    if not file_path:
        return ""

    file_name = file_path.split("/")[-1]

    if "." not in file_name:
        return ""

    if file_name.startswith(".") and file_name.count(".") == 1:
        return ""

    return file_name.split(".")[-1]


def _parse_json(data: str) -> Any:
    return json.loads(data)


def _parse_yaml(data: str) -> Any:
    return yaml.safe_load(data)


YAML_EXTENSIONS = ('yaml', 'yml')

PARSERS = {'json': _parse_json}
PARSERS.update(dict.fromkeys(YAML_EXTENSIONS, _parse_yaml))


def _parse_data(data: str, extension: str) -> dict:
    parser = PARSERS.get(extension)

    if not parser:
        raise ValueError(f'Unsupported extension: {extension}')

    if not data.strip():
        return {}

    result = parser(data)

    if not isinstance(result, dict):
        raise ValueError(f"{extension.upper()} must contain an object")

    return result


def _read_file(path: str) -> str:
    with open(path, mode='r', encoding='utf-8') as f:
        return f.read()


def read_and_parse_file(file_path: str) -> dict[Any, Any]:
    return _parse_data(
        _read_file(file_path), extension=get_file_extension(file_path))
