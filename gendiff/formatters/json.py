from __future__ import annotations

import json


def make_output(difference: dict) -> str:
    return json.dumps(difference, indent=4)
