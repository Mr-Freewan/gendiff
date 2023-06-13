import pytest
import os
from gendiff import generate_diff


def get_path(file):
    return os.path.join('tests', 'fixtures', file)

@pytest.mark.parametrize(('file1_path', 'file2_path', 'formatter', 'expected'),
                         [
                            ('file1_flat.json',
                             'file2_flat.json',
                             'stylish',
                             'correct_json_flat_stylish_output.txt'),

                            ('file1_flat.json',
                             'file2_flat.json',
                             'json',
                             'correct_json_flat_json_output.txt'),

                            ('file1_nested.json',
                             'file2_nested.json',
                             'stylish',
                             'correct_json_nested_stylish_output.txt'),

                            ('file1_nested.json',
                             'file2_nested.json',
                             'json',
                             'correct_json_nested_json_output.txt'),                            
                         ])
def test_generate_diff(file1_path, file2_path, formatter, expected):
    expected_path = get_path(expected)
    with open(expected_path, 'r') as file:
        result_data = file.read()
        test_path1 = get_path(file1_path)
        test_path2 = get_path(file2_path)
        assert generate_diff(test_path1, test_path2, formatter) == result_data