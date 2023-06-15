from __future__ import annotations

import argparse


DESCRIPTION = 'Compares two configuration files and shows a difference.'
FORMATTERS = (
    'stylish',
    'json',
    'plain'
)


def get_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('first_file',
                        type=str,
                        help='the path of the first file to compare')
    parser.add_argument('second_file',
                        type=str,
                        help='the path of the second file to compare')
    parser.add_argument('-f', '--format',
                        type=str,
                        choices=FORMATTERS,
                        default='stylish',
                        help='set format of output. Default is stylish')

    return parser.parse_args()


def message_not_supported(extension: str, supported: tuple[str]) -> None:
    print(f'{extension} extension is not supported. '
          f'{supported} supported only')


def message_not_exists(path: str) -> None:
    print(f'File {path} is not exists')


def diff_message(output: str) -> None:
    print(output)
