import json

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


def _parse_json(data: str) -> dict:
    return json.loads(data)


def _parse_yaml(data: str) -> dict:
    return yaml.safe_load(data)


YAML_EXTENSIONS = ('yaml', 'yml')

PARSERS = {'json': _parse_json}
PARSERS.update(dict.fromkeys(YAML_EXTENSIONS, _parse_yaml))


def parse_data(data: str, extension: str) -> dict:
    parser = PARSERS.get(extension)

    if not parser:
        raise ValueError(f'Unsupported extension: {extension}')

    if not data.strip():
        return {}

    return parser(data)
