from __future__ import annotations

from gendiff.file_reader import get_data
from gendiff.formatters import json, plain, stylish


EXPECTED_FORMATTERS = {
    'json': json,
    'plain': plain,
    'stylish': stylish
}


def find_difference(data_1: dict, data_2: dict) -> list[dict]:
    all_keys = sorted(data_1.keys() | data_2.keys())
    difference = {}

    for key in all_keys:
        node = {}

        if key not in data_1:
            node['status'] = 'added'
            node['data'] = data_2[key]

        elif key not in data_2:
            node['status'] = 'removed'
            node['data'] = data_1[key]

        elif data_1[key] == data_2[key]:
            node['status'] = 'not changed'
            node['data'] = data_1[key]

        elif isinstance(data_1[key], dict) and isinstance(data_2[key], dict):
            node['status'] = 'nested'
            node['children'] = find_difference(data_1[key], data_2[key])

        else:
            node['status'] = 'changed'
            node['old_data'] = data_1[key]
            node['new_data'] = data_2[key]

        difference[key] = node

    return difference


def generate_diff(file1_path: str,
                  file2_path: str,
                  formatter_type: str = 'stylish') -> str | None:
    data_1 = get_data(file1_path)
    data_2 = get_data(file2_path)

    difference = find_difference(data_1, data_2)

    formatter = EXPECTED_FORMATTERS.get(formatter_type)

    return formatter.make_output(difference)
