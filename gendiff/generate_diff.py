from typing import Any

from .file_utils import read_and_parse_file
from .formatters import format_json, format_plain, format_stylish


def _build_diff(dict1: dict[Any, Any],
                dict2: dict[Any, Any]) -> list[dict[str, Any]]:
    all_keys = sorted(set(dict1.keys()).union(dict2.keys()))
    diff = []
    for key in all_keys:
        if key not in dict1:
            info = {'key': key, 'type': 'added'}
            info['value'] = dict2[key]

        elif key not in dict2:
            info = {'key': key, 'type': 'removed'}
            info['value'] = dict1[key]

        elif dict1[key] == dict2[key]:
            info = {'key': key, 'type': 'unchanged'}
            info['value'] = dict1[key]

        else:
            info = {'key': key, 'type': 'updated'}
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                info['type'] = 'nested'
                info['children'] = _build_diff(dict1[key], dict2[key])
            else:
                info['value'] = (dict1[key], dict2[key])

        diff.append(info)
    return diff


FORMATTERS = {
    'stylish': format_stylish,
    'plain': format_plain,
    'json': format_json
}


def generate_diff(file1_path: str, file2_path: str,
                  format_name: str = 'stylish') -> str:
    file1_dict = read_and_parse_file(file1_path)
    file2_dict = read_and_parse_file(file2_path)
    diff = _build_diff(file1_dict, file2_dict)
    formatter = FORMATTERS.get(format_name)
    if formatter is None:
        raise ValueError(f'Unsupported format type: {format_name}')
    return formatter(diff)
