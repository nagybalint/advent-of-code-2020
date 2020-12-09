import os
from typing import List
from task1 import parse_input

TARGET_NUM = 248131121

def calculate_answer(in_list: List[int]) -> int:
    h = 1
    l = 0
    while h < len(in_list):
        sublist = in_list[l : h + 1]
        sum_of_sublist = sum(sublist)
        if sum_of_sublist == TARGET_NUM:
            return min(sublist) + max(sublist)
        elif sum_of_sublist > TARGET_NUM:
            l += 1
        elif sum_of_sublist < TARGET_NUM:
            h += 1

        if h == l:
            h += 1
        
if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    in_list = parse_input(file_path)
    answer = calculate_answer(in_list)
    print(answer)