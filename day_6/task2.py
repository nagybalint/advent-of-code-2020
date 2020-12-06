import os
from typing import List
from task1 import parse_input

def calculate_answer(in_list: List[List[str]]) -> int:
    num_of_yes_questions = 0
    for elem in in_list:
        if len(elem) == 1:
            num_of_yes_questions += len(elem[0])
        else:
            sets = [set(x) for x in elem]
            common_letters = sets[0].intersection(*sets[1:])
            num_of_yes_questions += len(common_letters)
    return num_of_yes_questions

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    in_list = parse_input(file_path)
    answer = calculate_answer(in_list)
    print(answer)