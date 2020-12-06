import os
from typing import List

def parse_input(file_name: str) -> List[List[str]]:
    with open(file_name) as in_file:
        groups = [[]]
        for line in in_file.readlines():
            if line.strip() == "":
                groups.append([])
            else:
                groups[-1].extend([line.strip()])
        return groups

def calculate_answer(in_list: List[List[str]]) -> int:
    num_of_yes_questions = 0
    for elem in in_list:
        num_of_yes_questions += len(set("".join(elem)))
    return num_of_yes_questions

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    in_list = parse_input(file_path)
    answer = calculate_answer(in_list)
    print(answer)