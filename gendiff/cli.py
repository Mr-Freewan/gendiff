from __future__ import annotations

import argparse


DESCRIPTION = 'Compares two configuration files and shows a difference.'


def get_arguments() -> argparse.Namespace:
    """
    Gets the specified arguments from the command line

    Returns:
        argparse.Namespace: Value of arguments
    """
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('first_file',
                        type=str,
                        help='the path of the first file to compare')
    parser.add_argument('second_file',
                        type=str,
                        help='the path of the second file to compare')
    parser.add_argument('-f', '--format',
                        type=str,
                        choices=(
                            'stylish',
                            'json',
                            'plain'
                        ),
                        default='stylish',
                        help='set format of output. Default is stylish')

    return parser.parse_args()


def message_not_supported(extension: str, supported: tuple[str]) -> None:
    """
    Prints a warning if a file with an unsupported extension is transmitted

    Args:
        extension (str): Extension of file
        supported (tuple[str]): Supported extensions
    """
    print(f'{extension} extension is not supported. '
          f'{supported} supported only')


def message_not_exists(path: str) -> None:
    """
    Prints a warning if a file not exists or parh is wrong

    Args:
        path (str): Path of file
    """
    print(f'File {path} is not exists')
