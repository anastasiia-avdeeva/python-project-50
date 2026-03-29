from .formatters import stylish


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


FORMATTERS = {
    'stylish': stylish,
}


def generate_diff(dict1, dict2, format_name='stylish'):
    diff = _build_diff(dict1, dict2)
    formatter = FORMATTERS[format_name]
    return formatter(diff)
