import argparse


def createParser():
    parser = argparse.ArgumentParser(
        usage='gendiff [-h] first_file second_file',
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    return parser


def main():
    parser = createParser()
    parser.parse_args()


if __name__ == '__main__':
    main()
