import os
from typing import List, Tuple

def parse_input(file_name: str) -> List[str]:
    with open(file_name) as f:
        return [line.strip() for line in f.readlines()]

def calculate_answer(instructions: List[str]) -> int:
    mem = {}
    or_mask = and_mask = 0
    for i in instructions:
        if i.startswith('mask'):
            or_mask, and_mask = get_masks(i)
        else:
            expr = f'{i} & {and_mask} | {or_mask}'
            exec(expr)
    return sum([val for val in mem.values()])

def get_masks(mask_instruction: str) -> Tuple[int, int]:

    mask_value = mask_instruction.split(' = ')[1]
    or_mask = int(mask_value.replace('X', '0'), 2)
    and_mask = int(mask_value.replace('X', '1'), 2)

    return or_mask, and_mask

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    instructions = parse_input(file_path)
    answer = calculate_answer(instructions)
    print(answer)