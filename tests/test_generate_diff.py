import pytest

from gendiff import generate_diff


@pytest.fixture
def dict1_flat():
    return {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False,
        "baz": None
    }


@pytest.fixture
def dict2_flat():
    return {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }


def test_generate_diff_flat(dict1_flat, dict2_flat):
    expected = '''{
  - baz: null
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert generate_diff(dict1_flat, dict2_flat) == expected
    assert dict1_flat == {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False,
        "baz": None
    }
    assert dict2_flat == {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }


def test_generate_diff_empty_dicts():
    expected = '{\n}'
    assert generate_diff({}, {}) == expected


def test_generate_diff_one_empty_dict(dict1_flat):
    expected = '''{
  - baz: null
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}'''

    assert generate_diff(dict1_flat, {}) == expected
