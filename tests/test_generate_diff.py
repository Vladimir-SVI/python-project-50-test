import ast
from gendiff import generate_diff
from gendiff.parsing import parse


def test_generate_diff():
    diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    file = open('tests/fixtures/correct_result.txt', 'r')
    result = file.read()[:-1]
    assert diff == result


def test_generate_diff_yml():
    diff = generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')
    file = open('tests/fixtures/correct_result.txt', 'r')
    result = file.read()[:-1]
    assert diff == result


def test_parse():
    parse_test = parse('tests/fixtures/file1.json')
    file = open('tests/fixtures/parse_result.py', 'r')
    string = file.read()
    res_dict = ast.literal_eval(string)
    assert parse_test == res_dict
