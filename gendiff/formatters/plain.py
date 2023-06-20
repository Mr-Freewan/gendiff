from __future__ import annotations

from typing import Any


JSON_TRANSLATOR = {
    'True': "true",
    'False': "false",
    'None': "null"
}


def make_child_string(data: Any) -> str:
    """
    Makes line of changes for values

    Args:
        data (Any): Value of some key

    Returns:
        str: Changed value in plain format
    """
    child_string = str(data)

    if isinstance(data, dict) or isinstance(data, list):
        child_string = '[complex value]'

    elif isinstance(data, str):
        child_string = f"'{data}'"

    return JSON_TRANSLATOR.get(child_string, child_string)


def make_node_string(key: str, data: dict, path: str) -> str:
    """
    Makes line of changes for keys

    Args:
        key (str): Key for which the line is makes
        data (dict): Dictionary of differences
        path (str): Path to changing, consisting of parent keys

    Returns:
        str: Change string for the key
    """
    status = data[key].get('status')
    node_string = ''

    if status == 'added':
        value = make_child_string(data[key]["data"])
        node_string = f"Property '{path}' was added with value: {value}"

    elif status == 'removed':
        node_string = f"Property '{path}' was removed"

    elif status == 'changed':
        value_old = make_child_string(data[key]["old_data"])
        value_new = make_child_string(data[key]["new_data"])
        node_string = f"Property '{path}' was updated. " \
                      f"From {value_old} to {value_new}"

    return node_string


def make_output(difference: dict) -> str:
    """
    Makes string of differencies in plain format

    Args:
        difference (dict): Dictionary of differences

    Returns:
        str: String of differencies in plain format
    """
    result = []

    def collect_lines(data: Any, path: list) -> None:
        """
        Traverses the dictionary in depth and fills the external list
        with strings of changes in plain format

        Args:
            data (Any): Dictionary of differences or key/value
            path (list): Path to changing, consisting of parent keys
        """
        for key in data:
            status = data[key].get('status')

            if status == 'nested':
                collect_lines(data[key]['children'], path + [key])
                continue

            path_to_change = '.'.join(path + [key])
            change_string = make_node_string(key, data, path_to_change)
            if change_string:
                result.append(change_string)

    collect_lines(difference, [])

    return '\n'.join(result)
