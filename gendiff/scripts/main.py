import argparse

from gendiff import generate_diff


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage='gendiff [-h] [-f FORMAT] first_file second_file',
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        default='stylish',
        help='set format of output'
    )
    return parser


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()
    file1_path = args.first_file
    file2_path = args.second_file
    format_name = args.format
    diff = generate_diff(file1_path, file2_path, format_name)
    print(diff)


if __name__ == '__main__':
    main()
