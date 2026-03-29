from typing import Union, cast

from .formatters_utils import _transform_val


def _format_val(value: Union[dict, str, bool, int, float, None]) -> str:
    if isinstance(value, dict):
        return "[complex value]"

    transformed = _transform_val(value)
    without_quotes = ['true', 'false', 'null']

    if transformed in without_quotes:
        return transformed

    return f"'{transformed}'"


def format_plain(diff: list[dict], parents: str = '') -> str:
    lines = []
    for item in diff:
        node_type = item['type']
        key = item['key']
        value = item.get('val')
        path = parents + "." + key if parents else key

        if node_type == "nested":
            children = item.get("children", [])
            lines.extend(format_plain(children, path).split("\n"))
            continue

        elif node_type == "added":
            formatted_val = _format_val(value)
            line = f"Property '{path}' was added with value: {formatted_val}"

        elif node_type == "updated":
            old_val, new_val = cast(tuple, value)
            formatted_old = _format_val(old_val)
            formatted_new = _format_val(new_val)
            line = f"Property '{path}' was updated. "
            line += f"From {formatted_old} to {formatted_new}"

        elif node_type == "removed":
            line = f"Property '{path}' was removed"

        else:
            continue

        lines.append(line)
    return "\n".join(lines)
