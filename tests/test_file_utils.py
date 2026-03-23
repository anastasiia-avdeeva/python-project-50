import pytest

from gendiff import get_file_extension


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
