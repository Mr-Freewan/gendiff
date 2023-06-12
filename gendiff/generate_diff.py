from gendiff.file_reader import get_data


def generate_diff(file1, file2, formatter):
    data_1 = get_data(file1)
    data_2 = get_data(file2)
    print(data_1, data_2)
