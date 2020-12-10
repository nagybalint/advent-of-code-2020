import os
from typing import List
from task1 import parse_input

ways_of_finishing_from_index = {}

def calculate_answer(in_list: List[int]) -> int:
    in_list.sort()
    in_list = [0] + in_list + [in_list[-1] + 3]
    return get_ways_to_finish_from(0, in_list)

def get_ways_to_finish_from(index: int, in_list: List[int]) -> int:
    if index in ways_of_finishing_from_index:
        return ways_of_finishing_from_index[index]
    
    if index >= len(in_list) - 2:
        ways_of_finishing_from_index[index] = 1
        return 1
    if index == len(in_list) - 3:
        if in_list[index + 2] - in_list[index] <= 3:
            ways_of_finishing_from_index[index] = 2
            return 2
        else:
            ways_of_finishing_from_index[index] = 1
            return 1
    
    num_of_ways = get_ways_to_finish_from(index + 1, in_list)
    if in_list[index + 2] - in_list[index] <= 3:
        num_of_ways += get_ways_to_finish_from(index + 2, in_list)
    if in_list[index + 3] - in_list[index] <= 3:
        num_of_ways += get_ways_to_finish_from(index + 3, in_list)
    ways_of_finishing_from_index[index] = num_of_ways
    return num_of_ways

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    in_list = parse_input(file_path)
    answer = calculate_answer(in_list)
    print(answer)