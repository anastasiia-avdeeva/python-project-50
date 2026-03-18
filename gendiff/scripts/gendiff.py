import argparse
import json


def createParser():
    parser = argparse.ArgumentParser(
        usage='gendiff [-h] [-f FORMAT] first_file second_file',
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output'
    )
    return parser


def parse_json(file_path):
    with open(file_path) as file:
        return json.load(file)


def main():
    parser = createParser()
    args = parser.parse_args()
    first_file, second_file = args.first_file, args.second_file
    file1_dict = parse_json(first_file)
    file2_dict = parse_json(second_file)


if __name__ == '__main__':
    main()
