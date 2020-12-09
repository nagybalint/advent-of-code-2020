import os
from typing import List

PREABMLE_LENGTH = 25

def parse_input(file_name: str) -> List[int]:
    with open(file_name) as in_file:
        return [int(line.strip()) for line in in_file.readlines()]

def is_sum_of_any_two(target: int, nums: List[int]) -> bool:
    for elem in nums:
        if elem * 2 == target:
            continue
        if (target - elem in nums):
            return True
    else:
        return False

def calculate_answer(in_list: List[int]) -> int:
    for i in range(PREABMLE_LENGTH, len(in_list)):
        if not is_sum_of_any_two(in_list[i], in_list[i - PREABMLE_LENGTH : i]):
            return in_list[i]
    else:
        return -1

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    in_list = parse_input(file_path)
    answer = calculate_answer(in_list)
    print(answer)