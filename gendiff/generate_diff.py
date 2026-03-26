PREFIXES = {'added': '+ ', 'removed': '- ', 'unchanged': '  ', 'nested': '  '}
INDENT = 4
SIGN_OFFSET = 2


def _build_diff(dict1, dict2):
    all_keys = sorted(set(dict1.keys()).union(dict2.keys()))
    diff = []
    for key in all_keys:
        if key not in dict1:
            info = {'key': key, 'type': 'added'}
            info['val'] = dict2[key]

        elif key not in dict2:
            info = {'key': key, 'type': 'removed'}
            info['val'] = dict1[key]

        elif dict1[key] == dict2[key]:
            info = {'key': key, 'type': 'unchanged'}
            info['val'] = dict1[key]

        else:
            info = {'key': key, 'type': 'changed'}
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                info['type'] = 'nested'
                info['children'] = _build_diff(dict1[key], dict2[key])
            else:
                info['val'] = (dict1[key], dict2[key])

        diff.append(info)
    return diff


def _transform_val(value):
    from_to = {None: 'null', True: 'true', False: 'false'}
    return from_to.get(value, value)


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


def _format_diff_stylish(diff, depth=1):
    indent = ' ' * (depth * INDENT - SIGN_OFFSET)
    lines = ['{']
    for item in diff:
        node_type = item['type']
        key = item['key']
        value = item.get('val')
        children = item.get('children')

        if node_type == 'nested':
            prefix = PREFIXES["nested"]
            value_str = _format_diff_stylish(children, depth + 1)
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


FORMATTERS = {
    'stylish': _format_diff_stylish,
}


def generate_diff(dict1, dict2, format_name='stylish'):
    diff = _build_diff(dict1, dict2)
    formatter = FORMATTERS[format_name]
    return formatter(diff)
