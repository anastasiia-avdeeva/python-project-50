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


EXPECTED_FLAT_STYLISH = '''{
  - baz: null
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_generate_diff_stylish_flat(dict1_flat, dict2_flat):
    assert generate_diff(dict1_flat, dict2_flat) == EXPECTED_FLAT_STYLISH
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


def test_generate_diff_stylish_empty_dicts_():
    expected = '{\n}'
    assert generate_diff({}, {}) == expected


def test_generate_diff_stylish_one_empty_dict(dict1_flat):
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


EXPECTED_NESTED_STYLISH = '''{
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


def test_generate_diff_stylish_nested(dict1_nested, dict2_nested):
    assert generate_diff(dict1_nested, dict2_nested) == EXPECTED_NESTED_STYLISH


EXPECTED_FLAT_PLAIN = """Property 'baz' was removed
Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From '50' to '20'
Property 'verbose' was added with value: true"""


def test_generate_diff_plain_flat(dict1_flat, dict2_flat):
    assert generate_diff(dict1_flat, dict2_flat,
                         'plain') == EXPECTED_FLAT_PLAIN


EXPECTED_NESTED_PLAIN = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""


def test_generate_diff_plain_nested(dict1_nested, dict2_nested):
    assert generate_diff(dict1_nested, dict2_nested,
                         'plain') == EXPECTED_NESTED_PLAIN


EXPECTED_FLAT_JSON = '''[
    {
        "key": "baz",
        "type": "removed",
        "value": null
    },
    {
        "key": "follow",
        "type": "removed",
        "value": false
    },
    {
        "key": "host",
        "type": "unchanged",
        "value": "hexlet.io"
    },
    {
        "key": "proxy",
        "type": "removed",
        "value": "123.234.53.22"
    },
    {
        "key": "timeout",
        "type": "updated",
        "value": [
            50,
            20
        ]
    },
    {
        "key": "verbose",
        "type": "added",
        "value": true
    }
]'''


def test_generate_diff_json_flat(dict1_flat, dict2_flat):
    assert generate_diff(dict1_flat, dict2_flat,
                         'json') == EXPECTED_FLAT_JSON


EXPECTED_NESTED_JSON = '''[
    {
        "key": "common",
        "type": "nested",
        "children": [
            {
                "key": "follow",
                "type": "added",
                "value": false
            },
            {
                "key": "setting1",
                "type": "unchanged",
                "value": "Value 1"
            },
            {
                "key": "setting2",
                "type": "removed",
                "value": 200
            },
            {
                "key": "setting3",
                "type": "updated",
                "value": [
                    true,
                    null
                ]
            },
            {
                "key": "setting4",
                "type": "added",
                "value": "blah blah"
            },
            {
                "key": "setting5",
                "type": "added",
                "value": {
                    "key5": "value5"
                }
            },
            {
                "key": "setting6",
                "type": "nested",
                "children": [
                    {
                        "key": "doge",
                        "type": "nested",
                        "children": [
                            {
                                "key": "wow",
                                "type": "updated",
                                "value": [
                                    "",
                                    "so much"
                                ]
                            }
                        ]
                    },
                    {
                        "key": "key",
                        "type": "unchanged",
                        "value": "value"
                    },
                    {
                        "key": "ops",
                        "type": "added",
                        "value": "vops"
                    }
                ]
            }
        ]
    },
    {
        "key": "group1",
        "type": "nested",
        "children": [
            {
                "key": "baz",
                "type": "updated",
                "value": [
                    "bas",
                    "bars"
                ]
            },
            {
                "key": "foo",
                "type": "unchanged",
                "value": "bar"
            },
            {
                "key": "nest",
                "type": "updated",
                "value": [
                    {
                        "key": "value"
                    },
                    "str"
                ]
            }
        ]
    },
    {
        "key": "group2",
        "type": "removed",
        "value": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    },
    {
        "key": "group3",
        "type": "added",
        "value": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
]'''


def test_generate_diff_json_nested(dict1_nested, dict2_nested):
    assert generate_diff(dict1_nested, dict2_nested,
                         'json') == EXPECTED_NESTED_JSON


def test_generate_diff_unsupported_format(dict1_nested, dict2_nested):
    with pytest.raises(ValueError):
        generate_diff(dict1_nested, dict2_nested, 'any format')
