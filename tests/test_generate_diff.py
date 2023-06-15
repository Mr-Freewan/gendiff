from __future__ import annotations

import os

import pytest
from gendiff import generate_diff


def get_path(file: str) -> str:
    return os.path.join('tests', 'fixtures', file)


@pytest.mark.parametrize(('file1_path', 'file2_path', 'formatter', 'expected'),
                         [
                             # Flat structure and stylish output
                             # JSON
                             ('file1_flat.json',
                              'file2_flat.json',
                              'stylish',
                              'correct_flat_stylish_output.txt'),
                             # YAML
                             ('file1_flat.yml',
                              'file2_flat.yaml',
                              'stylish',
                              'correct_flat_stylish_output.txt'),
                             # Flat structure and JSON output
                             ('file1_flat.json',
                              'file2_flat.json',
                              'json',
                              'correct_flat_json_output.txt'),
                             # Flat structure and plain output
                             ('file1_flat.json',
                              'file2_flat.json',
                              'plain',
                              'correct_flat_plain_output.txt'),
                             # Nested structure and stylish output
                             # JSON
                             ('file1_nested.json',
                              'file2_nested.json',
                              'stylish',
                              'correct_nested_stylish_output.txt'),
                             # YAML
                             ('file1_nested.yaml',
                              'file2_nested.yml',
                              'stylish',
                              'correct_nested_stylish_output.txt'),
                             # Nested structure and JSON output
                             ('file1_nested.yaml',
                              'file2_nested.yml',
                              'json',
                              'correct_nested_json_output.txt'),
                             # Nested structure and plain output
                             ('file1_nested.yaml',
                              'file2_nested.yml',
                              'plain',
                              'correct_nested_plain_output.txt'),
                             # Equal Files
                             ('file1_nested.json',
                              'file1_nested.json',
                              'stylish',
                              'correct_nested_equal_stylish_output.txt')])
def test_generate_diff(file1_path: str, file2_path: str,
                       formatter: str, expected: str) -> None:
    expected_path = get_path(expected)
    with open(expected_path, 'r') as file:
        result_data = file.read()
        test_path1 = get_path(file1_path)
        test_path2 = get_path(file2_path)
        assert generate_diff(test_path1, test_path2, formatter) == result_data


@pytest.mark.parametrize(('file1_path', 'file2_path', 'formatter'),
                         [
                             # Wrong extension
                             ('file1_nested.txt',
                              'file2_nested.json',
                              'stylish'),
                             # File not exists
                             ('file1.json',
                              'file2_nested.json',
                              'stylish')])
def test_wrong_files_sys_exit(file1_path: str, file2_path: str,
                              formatter: str) -> None:
    test_path1 = get_path(file1_path)
    test_path2 = get_path(file2_path)
    with pytest.raises(SystemExit) as sys_exit:
        generate_diff(test_path1, test_path2, formatter)
    assert sys_exit.type == SystemExit
    assert sys_exit.value.code == 1
