from gendiff import generate_diff


def test_generate_diff():
    diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    file = open('tests/fixtures/correct_result.txt', 'r')
    result = file.read()[:-1]
    assert diff == result
