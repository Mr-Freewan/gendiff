#!/usr/bin/env python3
from gendiff import generate_diff, cli


def main():
    args = cli.get_arguments()

    output = generate_diff(args.first_file,
                           args.second_file,
                           args.format)
    cli.diff_message(output)


if __name__ == "__main__":
    main()
