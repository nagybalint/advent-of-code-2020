import os
from typing import Dict
from task1 import parse_input

def calculate_answer(bags: Dict[str, Dict[str, int]], color: str) -> int:
    return get_contained_bags(bags, color)

def get_contained_bags(bags: Dict[str, Dict[str, int]], color: str) -> int:
    bags_contained = 0
    for k, v in bags[color].items():
        bags_contained += v * (1 + get_contained_bags(bags, k))
    return bags_contained

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    bags = parse_input(file_path)
    answer = calculate_answer(bags, "shiny gold")
    print(answer)