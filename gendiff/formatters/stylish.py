from __future__ import annotations

from typing import Any


INDENT_CHAR = ' '
INDENT_COUNT = 4  # Must be > 2
INDENT_LEVEL = INDENT_CHAR * INDENT_COUNT

JSON_TRANSLATOR = {
    'True': 'true',
    'False': 'false',
    'None': 'null'
}


def translate_to_json_format(data: Any) -> str:
    if str(data) in JSON_TRANSLATOR:
        return JSON_TRANSLATOR[str(data)]

    return str(data)


def make_child_string(data: Any, indent: str) -> str:
    if not isinstance(data, dict):
        return translate_to_json_format(data)

    node_indent = indent
    value_indent = indent + INDENT_LEVEL
    lines = []

    for key in data:
        value = make_child_string(data[key], value_indent)
        lines.append(f'{value_indent}{key}: {value}\n')

    return ''.join(['{\n', *lines, node_indent + '}'])


def make_node_string(key: str, data: Any, indent: str) -> str:
    status = data[key].get('status')
    node_string = ''

    if status == 'not changed':
        child_string = make_child_string(data[key]["data"], indent)
        node_string = f'{indent}{key}: {child_string}\n'

    elif status == 'added':
        child_string = make_child_string(data[key]["data"], indent)
        node_string = f'{indent[:-2]}+{INDENT_CHAR}{key}: {child_string}\n'

    elif status == 'removed':
        child_string = make_child_string(data[key]["data"], indent)
        node_string = f'{indent[:-2]}-{INDENT_CHAR}{key}: {child_string}\n'

    elif status == 'changed':
        child_string_old = make_child_string(data[key]["old_data"], indent)
        child_string_new = make_child_string(data[key]["new_data"], indent)
        old_string = f'{indent[:-2]}-{INDENT_CHAR}{key}: {child_string_old}\n'
        new_string = f'{indent[:-2]}+{INDENT_CHAR}{key}: {child_string_new}\n'
        node_string = old_string + new_string

    return node_string


def make_output(difference: dict) -> str:
    result = []

    def collect_lines(data: Any, level: int) -> None:
        indent = INDENT_LEVEL * level
        for key in data:
            if data[key].get('status') == 'nested':
                result.extend([f'{indent}{key}: ', '{\n'])
                collect_lines(data[key]['children'], level + 1)
                result.extend([indent, '}\n'])
            else:
                data_string = make_node_string(key, data, indent)
                result.append(data_string)

    collect_lines(difference, 1)

    return ''.join(['{\n', *result, '}'])
