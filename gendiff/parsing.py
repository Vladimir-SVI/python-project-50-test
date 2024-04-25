import json
import yaml


def parse(file):
    index = file.index('.')
    file_extension = file[index + 1:]
    if file_extension == 'json':
        with open(file, "r") as f:
            dict_result = json.load(f)
    if file_extension == 'yml' or file_extension == 'yaml':
        with open(file) as f:
            dict_result = yaml.safe_load(f)
    return dict_result
