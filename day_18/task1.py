import os
from typing import List, Generator

def parse_input(file_name: str) -> List[str]:
    with open(file_name) as f:
        return [line.strip().replace(' ', '') for line in f.readlines()]

def problem_iterator(problem: str) -> Generator[str, None, None]:
    for letter in list(problem):
        yield letter

def calculate_problem(problem: str) -> int:
    def _helper(p_it: Generator[str, None, None]) -> int:
        lhs = next(p_it)
        if lhs == ')':
            lhs = _helper(p_it)
        else:
            lhs = int(lhs)

        try:
            op = next(p_it)
            if op == '(':
                return lhs
            rhs = _helper(p_it)
            return eval(f'{lhs}{op}{rhs}')
        except:
            return lhs

    it = problem_iterator(problem[::-1])
    return _helper(it)

def calculate_answer(problems: List[str]) -> int:
    return sum([calculate_problem(p) for p in problems])

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    problems = parse_input(file_path)
    answer = calculate_answer(problems)
    print(answer)