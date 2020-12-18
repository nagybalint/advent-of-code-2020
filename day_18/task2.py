import ast
import os
from typing import List
from task1 import parse_input

class MagicNumber:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return MagicNumber(self.val * other.val)

    def __mul__(self, other):
        return MagicNumber(self.val + other.val)

def calculate_problem(problem: str) -> int:
    prepared_problem = problem
    for i in range(10):
        prepared_problem = prepared_problem.replace(str(i), f'MagicNumber({i})')
    prepared_problem = prepared_problem.replace('+', 'p').replace('*', '+').replace('p', '*')
    ret_val = {}
    exec(f'ret_val["res"]={prepared_problem}')
    return ret_val["res"].val

def calculate_answer(problems: List[str]) -> int:
    return sum([calculate_problem(p) for p in problems])

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    problems = parse_input(file_path)
    answer = calculate_answer(problems)
    print(answer)