import pytest

@pytest.mark.parametrize(('file1_path', 
                          'file2_path', 
                          'formatter', 
                          'expected'),
                         [
                             ('file1_flat.json', 
                              'file2_flat.json', 
                              'stylish', 
                              'correct_flat_diff_json.txt')
                         ])
def test_generate_diff(file1_path, file2_path, formatter, expected):
    ...
