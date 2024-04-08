import json


def generate_diff(first_file, second_file):
    def is_true_or_false(key_value):
        if key_value:
            key_value = 'true'
        if not key_value:
            key_value = 'false'
        return key_value
    with open(first_file) as f1, open(second_file) as f2:
        file1 = json.load(f1)
        file2 = json.load(f2)
        file1_tuple = sorted(file1.items())
        file2_tuple = sorted(file2.items())
        file1_list = [i[0] for i in file1_tuple]
        file2_list = [i[0] for i in file2_tuple]
        result = ['{', '\n']
        for i in file1_list:
            if i in file2_list and file1[i] == file2[i]:
                result.append(f'  {i}: {is_true_or_false(file1[i])}\n')
            elif i in file2_list and file1[i] != file2[i]:
                result.append(f'- {i}: {is_true_or_false(file1[i])}\n')
                result.append(f'+ {i}: {is_true_or_false(file2[i])}\n')
            elif i not in file2_list:
                result.append(f'- {i}: {is_true_or_false(file1[i])}\n')
        for i2 in file2_list:
            if i2 not in file1_list:
                result.append(f'+ {i2}: {is_true_or_false(file2[i2])}\n')
        result.append('}')
        return ' '.join(result)
