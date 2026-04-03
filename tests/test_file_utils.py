import pytest

# from gendiff import read_and_parse_file
from gendiff.file_utils import get_file_extension, read_and_parse_file


# tests for get_file_extensions
@pytest.fixture
def path():
    return '/lib/hello.json'


@pytest.fixture
def path_without_extension():
    return '/lib/hello'


@pytest.fixture
def complex_path():
    return '/lib/archive.tar.gz'


@pytest.fixture
def path_to_hidden_file():
    return '/lib/.env'


def test_get_file_extension(path):
    assert get_file_extension(path) == 'json'


def test_get_file_extension_empty_path():
    assert get_file_extension('') == ''


def test_get_file_extension_without_ext(path_without_extension):
    assert get_file_extension(path_without_extension) == ''


def test_get_file_extension_complex_path(complex_path):
    assert get_file_extension(complex_path) == 'gz'


def test_get_file_extension_hidden_file(path_to_hidden_file):
    assert get_file_extension(path_to_hidden_file) == ''


# tests for read_and_parse_file
@pytest.fixture
def test_data_dir():
    return './tests/test_data'


EXPECTED_JSON = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
}

EXPECTED_YML = {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
}


def test_read_and_parse_json(test_data_dir):
    json_path = test_data_dir + 'file1.json'
    assert read_and_parse_file(json_path) == EXPECTED_JSON


def test_read_and_parse_yml(test_data_dir):
    yml_path = test_data_dir + 'file2.yml'
    assert read_and_parse_file(yml_path) == EXPECTED_YML


def test_read_and_parse_unsupported_ext(test_data_dir):
    unsupported_ext_path = test_data_dir + 'unsupported_ext.txt'
    with pytest.raises(ValueError):
        read_and_parse_file(unsupported_ext_path)


def test_read_and_parse_empty_file(test_data_dir):
    empty_file_path = test_data_dir + 'file_empty.yaml'
    assert read_and_parse_file(empty_file_path) == {}


def test_read_and_parse_no_object(test_data_dir):
    no_obj_path = test_data_dir + 'list.json'
    with pytest.raises(ValueError):
        read_and_parse_file(no_obj_path)
