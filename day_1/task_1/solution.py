import os
from collections import defaultdict

TARGET_VALUE = 2020

def parse_input(file_name: str) -> []:
    with open(file_path) as in_file:
        return [int(line.strip()) for line in in_file.readlines()]

def build_input_dict(in_list: list) -> dict:
    in_dict = defaultdict(lambda: 0)
    for val in in_list:
        in_dict[val] += 1
    return in_dict

def calculate_answer(in_dict: dict) -> dict:
    half_of_target = TARGET_VALUE/2
    if TARGET_VALUE%2 == 0 and in_dict[half_of_target] > 1:
        return {"a": half_of_target, "b": half_of_target, "mul": half_of_target**2}
    for k in in_dict:
        if k == half_of_target:
            continue
        if TARGET_VALUE - k in in_dict:
            return {"a": k, "b": TARGET_VALUE - k , "mul": k*(TARGET_VALUE - k)}
    raise Exception()

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    in_list = parse_input(file_path)
    in_dict = build_input_dict(in_list)
    answer = calculate_answer(in_dict)
    print(f'a: {answer["a"]}, b: {answer["b"]}, mul: {answer["mul"]}')