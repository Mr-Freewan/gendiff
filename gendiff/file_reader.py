from __future__ import annotations
import os
import json
import yaml
from gendiff import cli


SUPPORTED_HANDLERS = {
    '.json': json.load,
    '.yaml': yaml.safe_load,
    '.yml': yaml.safe_load
}


def get_file_extension(file_path: str) -> str:
    _, file_extension = os.path.splitext(file_path)
    return file_extension


def is_supported(file_path: str) -> bool:
    file_extension = get_file_extension(file_path)

    if file_extension not in SUPPORTED_HANDLERS:
        return False

    return True


def get_data(file_path: str, cli_mode: bool=True) -> dict | None:
    supported = is_supported(file_path)
    extension = get_file_extension(file_path)

    if not supported:
        if cli_mode:
            cli.message_not_supported(extension,
                                      tuple(SUPPORTED_HANDLERS.keys()))
        return

    try:
        with open(file_path, 'r') as file:
            return SUPPORTED_HANDLERS[extension](file)

    except FileNotFoundError:
        if cli_mode:
            cli.message_not_exists(file_path)
        return
