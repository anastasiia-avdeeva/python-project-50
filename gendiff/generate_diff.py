PREFIXES = {'added': '+ ', 'removed': '- ', 'unchanged': '  '}


def _build_diff(dict1, dict2, all_keys):
    diff = []
    for key in all_keys:
        if key not in dict1:
            info = {'key': key, 'type': 'added', 'val': dict2[key]}

        elif key not in dict2:
            info = {'key': key, 'type': 'removed', 'val': dict1[key]}

        elif dict1[key] == dict2[key]:
            info = {'key': key, 'type': 'unchanged',
                    'val': dict1[key]}

        else:
            info = {'key': key, 'type': 'changed',
                    'old_val': dict1[key], 'new_val': dict2[key]}

        diff.append(info)
    return diff


def _format_diff(diff):
    lines = ['{']
    for item in diff:
        if item['type'] == 'changed':
            str1 = f'  {PREFIXES['removed']}{item['key']}: {item['old_val']}'
            str2 = f'  {PREFIXES['added']}{item['key']}: {item['new_val']}'
            line = str1 + '\n' + str2
        else:
            line = f'  {PREFIXES[item['type']]}{item['key']}: {item['val']}'
        lines.append(line)
    lines.append('}')
    return '\n'.join(lines)


def generate_diff(dict1, dict2):
    all_keys = sorted(set(dict1.keys()).union(dict2.keys()))
    diff = _build_diff(dict1, dict2, all_keys)
    formated_diff_str = _format_diff(diff)
    return formated_diff_str
