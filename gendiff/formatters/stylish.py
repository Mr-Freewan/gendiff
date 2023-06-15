from __future__ import annotations

from typing import Any


INDENT_CHAR = ' '
INDENT_COUNT = 4  # Must be > 2
INDENT_LEVEL = INDENT_CHAR * INDENT_COUNT  # indent for each lvl

JSON_TRANSLATOR = {
    'True': 'true',
    'False': 'false',
    'None': 'null'
}


def translate_to_json_format(data: Any) -> str:
    """
    Converts value to string format

    Args:
        data (Any): Value of some key

    Returns:
        str: Value in string format
    """
    if str(data) in JSON_TRANSLATOR:
        return JSON_TRANSLATOR[str(data)]

    return str(data)


def make_child_string(data: Any, indent: str) -> str:
    """
    Makes line of changes for values

    Args:
        data (Any): Value of some key
        indent (str): Changed value or key

    Returns:
        str: Value in stylish format
    """
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
    """
    Makes line of changes for keys

    Args:
        key (str): Key for which the line is makes
        data (Any): Dictionary of differences
        indent (str): Current indent level

    Returns:
        str: String of changes for the key in stylish format
    """
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
    """
    Makes string of differencies in stylish format

    Args:
        difference (dict): Dictionary of differences

    Returns:
        str: String of differencies in plain format
    """
    result = []

    def collect_lines(data: Any, level: int) -> None:
        """
        Traverses the dictionary in depth and fills the external list
        with strings of changes in stylish format

        Args:
            data (Any): Dictionary of differences or key/value
            level (int): Current indent level
        """
        indent = INDENT_LEVEL * level
        for key in data:
            if data[key].get('status') != 'nested':
                data_string = make_node_string(key, data, indent)
                result.append(data_string)
                continue

            result.extend([f'{indent}{key}: ', '{\n'])
            collect_lines(data[key]['children'], level + 1)
            result.extend([indent, '}\n'])

    collect_lines(difference, 1)

    return ''.join(['{\n', *result, '}'])
