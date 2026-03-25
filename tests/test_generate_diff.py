import pytest

from gendiff import generate_diff


@pytest.fixture
def first_dict():
    return {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False,
        "baz": None
    }


@pytest.fixture
def second_dict():
    return {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }


def test_generate_diff_flat(first_dict, second_dict):
    expected = '''{
  - baz: null
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert generate_diff(first_dict, second_dict) == expected
    assert first_dict == {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False,
        "baz": None
    }
    assert second_dict == {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }


def test_generate_diff_flat_empty_dicts():
    expected = '{\n}'
    assert generate_diff({}, {}) == expected


def test_generate_diff_one_flat_empty_dict(first_dict):
    expected = '''{
  - baz: null
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}'''

    assert generate_diff(first_dict, {}) == expected
