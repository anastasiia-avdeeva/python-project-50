def _transform_val(value):
    from_to = {None: 'null', True: 'true', False: 'false'}
    return from_to.get(value, value)
