import os
from task1 import parse_input, build_input_dict, calculate_answer, TARGET_VALUE

def get_answer(in_dict: dict, target: int) -> dict:
    for k in in_dict.keys():
        remainder = target - k
        in_dict[k] -= 1
        solution = calculate_answer(in_dict, remainder)
        if solution is None:
            in_dict[k] += 1
        else:
            solution['c'] = k
            solution['mul'] *= k
            return solution
    return None

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    in_list = parse_input(file_path)
    in_dict = build_input_dict(in_list)
    answer = get_answer(in_dict, TARGET_VALUE)
    print(f'a: {answer["a"]}, b: {answer["b"]}, c: {answer["c"]}, mul: {answer["mul"]}')
    