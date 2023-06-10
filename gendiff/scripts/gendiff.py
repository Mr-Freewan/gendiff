#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help='the path of the first file to compare')
    parser.add_argument('second_file', type=str, help='the path of the second file to compare')
    parser.add_argument('-f', '--format', 
                        type=str, default='json', 
                        help='set format of output. Can be plain, json (default) or stylish.')

    args = parser.parse_args()


if __name__ == "__main__":
    main()