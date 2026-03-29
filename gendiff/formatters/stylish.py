from .formatters_utils import _transform_val

PREFIXES = {'added': '+ ', 'removed': '- ', 'unchanged': '  ', 'nested': '  '}
INDENT = 4
SIGN_OFFSET = 2


def _format_val(value, depth):
    if not isinstance(value, dict):
        return _transform_val(value)

    lines = ['{']
    indent = ' ' * (depth * INDENT)

    for key, val in value.items():
        line = f'{indent}{key}: {_format_val(val, depth + 1)}'
        lines.append(line)

    last_ind = ' ' * ((depth - 1) * INDENT)
    lines.append(last_ind + '}')
    return '\n'.join(lines)


def format_stylish(diff, depth=1):
    indent = ' ' * (depth * INDENT - SIGN_OFFSET)
    lines = ['{']
    for item in diff:
        node_type = item['type']
        key = item['key']
        value = item.get('val')
        children = item.get('children')

        if node_type == 'nested':
            prefix = PREFIXES["nested"]
            value_str = format_stylish(children, depth + 1)
            line = f'{indent}{prefix}{key}: {value_str}'

        elif node_type == 'changed':
            prefix = PREFIXES['removed']
            old_val, new_val = value
            str1 = f'{indent}{prefix}{key}: {_format_val(old_val, depth + 1)}'
            prefix = PREFIXES['added']
            str2 = f'{indent}{prefix}{key}: {_format_val(new_val, depth + 1)}'
            line = str1 + '\n' + str2

        else:
            prefix = PREFIXES[node_type]
            line = f'{indent}{prefix}{key}: {_format_val(value, depth + 1)}'

        lines.append(line)
    last_ind = ' ' * ((depth - 1) * INDENT)
    lines.append(last_ind + '}')
    return '\n'.join(lines)
