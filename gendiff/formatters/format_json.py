import json
from typing import Any


def format_json(diff: list[dict[str, Any]]) -> str:
    return json.dumps(diff, indent=4)
