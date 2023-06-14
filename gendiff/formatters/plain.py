from __future__ import annotations


JSON_TRANSLATOR = {
    'True': "true",
    'False': "false",
    'None': "null"
}


def make_child_string(data) -> str:
    child_string = str(data)

    if isinstance(data, dict) or isinstance(data, list):
        child_string = '[complex value]'

    elif isinstance(data, str):
        child_string = f"'{data}'"

    elif str(data) in JSON_TRANSLATOR:
        child_string = JSON_TRANSLATOR[str(data)]

    return child_string


def make_node_string(key: str, data, path: str) -> str:
    status = data[key].get('status')
    node_string = ''

    if status == 'added':
        value = make_child_string(data[key]["data"])
        node_string = f"Property '{path}' was added with value: {value}\n"

    elif status == 'removed':
        node_string = f"Property '{path}' was removed\n"

    elif status == 'changed':
        value_old = make_child_string(data[key]["old_data"])
        value_new = make_child_string(data[key]["new_data"])
        node_string = f"Property '{path}' was updated. " \
                      f"From {value_old} to {value_new}\n"

    return node_string


def make_output(difference: dict) -> str:
    result = []

    def collect_lines(data, path: list):
        for key in data:
            if data[key].get('status') == 'nested':
                collect_lines(data[key]['children'], path + [key])
            else:
                path_to_change = '.'.join(path + [key])
                change_string = make_node_string(key, data, path_to_change)
                if change_string:
                    result.append(change_string)

    collect_lines(difference, [])

    return ''.join(result)[:-1]
