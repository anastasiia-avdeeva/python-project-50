import pytest

from gendiff import get_file_extension, parse_data


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


@pytest.fixture
def data():
    data = {
        'json': '''{"language": "Python",
"version": 3.11, "follow": false, "timeout": 40}''',
        'json_nested': '''{"common": {"Follow": false, "setting3": null, 
"key": 123}, "group3": {"deep": {"id": {"number": 45}}}}''',
        'yaml': '''language: Python
version: 3.11
follow: false
"timeout": 40''',
        'yaml_nested': '''common:
  Follow: false
  setting3: null
  key: 123
group3:
  deep:
    id:
      number: 45'''
    }
    return data


@pytest.fixture
def expected_dict_flat():
    return {
        'language': 'Python',
        'version': 3.11,
        'follow': False,
        'timeout': 40
    }


@pytest.fixture
def expected_dict_nested():
    return {
        "common": {
            "Follow": False,
            "setting3": None,
            "key": 123
        },
        "group3": {
            "deep": {
                "id": {
                    "number": 45
                }
            }
        }
    }


def test_parse_flat_data(data, expected_dict_flat):
    assert parse_data(data['json'], 'json') == expected_dict_flat
    assert parse_data(data['yaml'], 'yaml') == expected_dict_flat
    assert parse_data(data['yaml'], 'yml') == parse_data(data['yaml'], 'yaml')
    assert parse_data(data['json'], 'json') == parse_data(data['yaml'], 'yml')


def test_parse_nested_data(data, expected_dict_nested):
    assert parse_data(data['json_nested'], 'json') == expected_dict_nested
    assert parse_data(data['yaml_nested'], 'yaml') == expected_dict_nested
    assert parse_data(data['yaml_nested'], 'yml') == parse_data(
        data['yaml_nested'], 'yaml')
    assert parse_data(data['json_nested'], 'json') == parse_data(
        data['yaml_nested'], 'yml')
    return


def test_parse_data_empty_dict():
    assert parse_data('{}', 'json') == {}
    assert parse_data('{}', 'yml') == {}


def test_parse_data_0b():
    assert parse_data(' ', 'json') == {}
    assert parse_data(' ', 'yaml') == {}


def test_parse_data_usupported_ext(data):
    with pytest.raises(ValueError):
        parse_data(data['yaml'], 'txt')
