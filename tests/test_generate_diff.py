import pytest

from gendiff import generate_diff


@pytest.fixture
def test_data_dir():
    return './tests/test_data/'


@pytest.fixture
def flat_json_paths(test_data_dir):
    json1 = test_data_dir + 'file1.json'
    json2 = test_data_dir + 'file2.json'
    return json1, json2


@pytest.fixture
def flat_yaml_paths(test_data_dir):
    yaml1 = test_data_dir + 'file1.yaml'
    yaml2 = test_data_dir + 'file2.yml'
    return yaml1, yaml2


@pytest.fixture
def nested_json_paths(test_data_dir):
    json1 = test_data_dir + 'file1_nested.json'
    json2 = test_data_dir + 'file2_nested.json'
    return json1, json2


@pytest.fixture
def nested_yaml_paths(test_data_dir):
    yaml1 = test_data_dir + 'file1_nested.yaml'
    yaml2 = test_data_dir + 'file2_nested.yaml'
    return yaml1, yaml2


EXPECTED_FLAT_STYLISH = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_generate_diff_flat_stylish(flat_json_paths, flat_yaml_paths):
    json1_path, json2_path = flat_json_paths
    assert generate_diff(json1_path, json2_path) == EXPECTED_FLAT_STYLISH
    yaml1_path, yaml2_path = flat_yaml_paths
    assert generate_diff(yaml1_path, yaml2_path) == EXPECTED_FLAT_STYLISH
    assert generate_diff(json1_path, yaml2_path) == EXPECTED_FLAT_STYLISH


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


def test_generate_diff_nested_stylish(nested_json_paths, nested_yaml_paths):
    json1_path, json2_path = nested_json_paths
    assert generate_diff(json1_path, json2_path) == EXPECTED_NESTED_STYLISH
    yaml1_path, yaml2_path = nested_yaml_paths
    assert generate_diff(yaml1_path, yaml2_path) == EXPECTED_NESTED_STYLISH
    assert generate_diff(yaml1_path, json2_path) == EXPECTED_NESTED_STYLISH


EXPECTED_FLAT_PLAIN = """Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true"""


def test_generate_diff_flat_plain(flat_json_paths, flat_yaml_paths):
    json1_path, json2_path = flat_json_paths
    assert generate_diff(json1_path, json2_path,
                         'plain') == EXPECTED_FLAT_PLAIN
    yaml1_path, yaml2_path = flat_yaml_paths
    assert generate_diff(yaml1_path, yaml2_path,
                         'plain') == EXPECTED_FLAT_PLAIN
    assert generate_diff(json1_path, yaml2_path,
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


def test_generate_diff_nested_plain(nested_json_paths, nested_yaml_paths):
    json1_path, json2_path = nested_json_paths
    assert generate_diff(json1_path, json2_path,
                         'plain') == EXPECTED_NESTED_PLAIN
    yaml1_path, yaml2_path = nested_yaml_paths
    assert generate_diff(yaml1_path, yaml2_path,
                         'plain') == EXPECTED_NESTED_PLAIN
    assert generate_diff(yaml1_path, json2_path,
                         'plain') == EXPECTED_NESTED_PLAIN


EXPECTED_FLAT_JSON = '''[
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


def test_generate_diff_json_flat(flat_json_paths, flat_yaml_paths):
    json1_path, json2_path = flat_json_paths
    assert generate_diff(json1_path, json2_path, 'json') == EXPECTED_FLAT_JSON
    yaml1_path, yaml2_path = flat_yaml_paths
    assert generate_diff(yaml1_path, yaml2_path, 'json') == EXPECTED_FLAT_JSON
    assert generate_diff(json1_path, yaml2_path, 'json') == EXPECTED_FLAT_JSON


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


def test_generate_diff_json_nested(nested_json_paths, nested_yaml_paths):
    json1_path, json2_path = nested_json_paths
    assert generate_diff(json1_path, json2_path,
                         'json') == EXPECTED_NESTED_JSON
    yaml1_path, yaml2_path = nested_yaml_paths
    assert generate_diff(yaml1_path, yaml2_path,
                         'json') == EXPECTED_NESTED_JSON
    assert generate_diff(yaml1_path, json2_path,
                         'json') == EXPECTED_NESTED_JSON


def test_generate_diff_empty_files(test_data_dir):
    file1_path = test_data_dir + 'file_empty.json'
    file2_path = test_data_dir + 'file_empty.yaml'
    expected_stylish = '{\n}'
    assert generate_diff(file1_path, file2_path) == expected_stylish
    expected_plain = ''
    assert generate_diff(file1_path, file2_path, 'plain') == expected_plain
    expected_json = '[]'
    assert generate_diff(file1_path, file2_path, 'json') == expected_json


def test_generate_diff_unsupported_format(flat_json_paths):
    json1_path, json2_path = flat_json_paths
    with pytest.raises(ValueError):
        generate_diff(json1_path, json2_path, 'any format')


def test_generate_diff_erronious_files(test_data_dir, flat_json_paths):
    json1_path, json2_path = flat_json_paths
    unsupported_ext_file = test_data_dir + 'unsupported_ext.txt'
    with pytest.raises(ValueError):
        generate_diff(json1_path, unsupported_ext_file)
    json_without_obj = test_data_dir + 'list.json'
    with pytest.raises(ValueError):
        generate_diff(json_without_obj, json2_path, 'plain')
