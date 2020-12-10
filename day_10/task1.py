import os
from typing import List

PREABMLE_LENGTH = 25

def parse_input(file_name: str) -> List[int]:
    with open(file_name) as in_file:
        return [int(line.strip()) for line in in_file.readlines()]

def calculate_answer(in_list: List[int]) -> int:
    in_list.append(0)
    in_list.sort()
    diffs = {1: 0, 2: 0, 3: 1}
    for i in range(len(in_list) - 1):
        diffs[in_list[i + 1] - in_list[i]] += 1
    return diffs[1] * diffs[3]


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    in_list = parse_input(file_path)
    answer = calculate_answer(in_list)
    print(answer)