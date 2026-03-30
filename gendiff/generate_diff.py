from .formatters import plain, stylish


def _build_diff(dict1: dict, dict2: dict) -> list[dict]:
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
    'stylish': stylish,
    'plain': plain
}


def generate_diff(dict1: dict, dict2: dict,
                  format_name: str = 'stylish') -> str:

    diff = _build_diff(dict1, dict2)
    formatter = FORMATTERS.get(format_name)
    if formatter is None:
        raise ValueError(f'Ubsupported format type: {format_name}')
    return formatter(diff)
