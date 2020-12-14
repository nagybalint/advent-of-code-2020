import os
from typing import List
from task1 import parse_input

def calculate_answer(instructions: List[str]) -> int:
    mem = {}
    mask = ''
    for i in instructions:
        lh, rh = i.split(' = ')
        if i.startswith('mask'):
            mask = rh
        else:
            val = int(rh)
            addr = int(lh[4:-1])
            write_locations = get_address_list(mask, addr)
            for loc in write_locations:
                mem[loc] = val
    return sum([val for val in mem.values()])

def get_address_list(mask: str, addr: int) -> List[int]:
    # Prepare address
    prepared_addr = addr & int(mask.replace('0', '1').replace('X', '0'), 2)
    mask_list = get_mask_list(mask)
    return list(map(lambda m: m | prepared_addr, mask_list))


def get_mask_list(mask: str) -> List[int]:
    if 'X' not in mask:
        return [int(mask, 2)]
    return get_mask_list(mask.replace('X', '0', 1)) + get_mask_list(mask.replace('X', '1', 1))

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    instructions = parse_input(file_path)
    answer = calculate_answer(instructions)
    print(answer)