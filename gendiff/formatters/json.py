from __future__ import annotations

import json


def make_output(difference: dict) -> str:
    """
    Makes string of differencies in JSON format

    Args:
        difference (dict): Dictionary of differences

    Returns:
        str: String of differencies in JSON format
    """
    return json.dumps(difference, indent=4)
