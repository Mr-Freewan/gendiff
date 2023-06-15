from __future__ import annotations
import os
import json
import yaml
import sys
from gendiff import cli


SUPPORTED_READERS = {
    '.json': json.load,
    '.yaml': yaml.safe_load,
    '.yml': yaml.safe_load
}


def get_file_extension(file_path: str) -> str:
    _, file_extension = os.path.splitext(file_path)
    return file_extension


def is_supported(file_path: str) -> bool:
    file_extension = get_file_extension(file_path)

    if file_extension not in SUPPORTED_READERS:
        return False

    return True


def get_data(file_path: str) -> dict | SystemExit:
    supported = is_supported(file_path)
    extension = get_file_extension(file_path)

    if not supported:
        cli.message_not_supported(extension,
                                  tuple(SUPPORTED_READERS.keys()))
        sys.exit(1)

    try:
        with open(file_path, 'r') as file:
            reader = SUPPORTED_READERS.get(extension)
            return reader(file)

    except FileNotFoundError:
        cli.message_not_exists(file_path)
        sys.exit(1)
