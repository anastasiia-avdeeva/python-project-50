import argparse

from gendiff import generate_diff, get_file_extension, parse_data


def create_parser():
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


def read_file(path: str) -> str:
    with open(path, mode='r') as f:
        return f.read()


def read_and_parse_file(file_path: str) -> dict:
    return parse_data(
        read_file(file_path), extension=get_file_extension(file_path))


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()
    file1_dict = read_and_parse_file(args.first_file)
    file2_dict = read_and_parse_file(args.second_file)
    format_name = args.format
    diff = generate_diff(file1_dict, file2_dict, format_name)
    print(diff)


if __name__ == '__main__':
    main()
