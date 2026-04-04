from typing import Union


def _transform_val(value:
                   Union[int, float, str, bool, None]) -> int | float | str:
    match value:
        case None:
            return 'null'
        case True:
            return 'true'
        case False:
            return 'false'
        case _:
            return value
