#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help='The first file to compare')
    parser.add_argument('second_file', type=str, help='The second file to compare')

    args = parser.parse_args()


if __name__ == "__main__":
    main()