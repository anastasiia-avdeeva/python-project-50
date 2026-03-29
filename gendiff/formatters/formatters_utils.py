from typing import Union


def _transform_val(value: Union[int, float, str, bool, None]):
    from_to = {None: 'null', True: 'true', False: 'false'}
    return from_to.get(value, value)
