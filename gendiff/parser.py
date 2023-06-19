from __future__ import annotations

from typing import Any
import json
import yaml


SUPPORTED_PARSERS = {
    'json': json.load,
    'yaml': yaml.safe_load,
    'yml': yaml.safe_load
}


def parse(data: Any, data_format: str) -> dict | None:
    """
    Parse data from requests or files in supported format.
    Now supported JSON or YAML

    Args:
        data (Any): Data from request or _io.TextIOWrapper
        data_format (str): Format of data: 'json', 'yaml' or 'yml'

    Returns:
        dict | None: Data in dictionary format or None if format not supported
    """
    data_parser = SUPPORTED_PARSERS.get(data_format)

    if not data_parser:
        return

    return data_parser(data)