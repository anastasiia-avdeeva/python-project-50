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


@pytest.fixture
def dict1_nested():
    return {
        "common": {
            "setting1": "Value 1",
            "setting2": 200,
            "setting3": True,
            "setting6": {
                "key": "value",
                "doge": {
                    "wow": ""
                }
            }
        },
        "group1": {
            "baz": "bas",
            "foo": "bar",
            "nest": {
                "key": "value"
            }
        },
        "group2": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    }


@pytest.fixture
def dict2_nested():
    return {
        "common": {
            "follow": False,
            "setting1": "Value 1",
            "setting3": None,
            "setting4": "blah blah",
            "setting5": {
                "key5": "value5"
            },
            "setting6": {
                "key": "value",
                "ops": "vops",
                "doge": {
                    "wow": "so much"
                }
            }
        },
        "group1": {
            "foo": "bar",
            "baz": "bars",
            "nest": "str"
        },
        "group3": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }


EXPECTED_NEST = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''


def test_generate_diff_nested(dict1_nested, dict2_nested):
    assert generate_diff(dict1_nested, dict2_nested) == EXPECTED_NEST
