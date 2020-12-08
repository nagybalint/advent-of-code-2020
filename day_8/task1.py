import os
from typing import List, Tuple

def parse_input(file_name: str) -> List[str]:
    with open(file_name) as in_file:
        return [line.strip() for line in in_file.readlines()]

def get_state_diff(command: str, current_pos: int, currect_acc: int) -> Tuple[int, int]:
    cmd_type, num = parse_command(command)
    if cmd_type == "nop":
        return 1, 0
    elif cmd_type == "acc":
        return 1, num
    elif cmd_type == "jmp":
        return num, 0
    else:
        raise Exception("Illegal command type")

def parse_command(command: str) -> Tuple[str, int]:
    cmd_type = command[:3]
    num = int(command[4:])
    return cmd_type, num

def calculate_answer(command_list: List[str]) -> int:
    pos = acc = 0
    pos_seen = set([0])
    while pos < len(command_list):
        command = command_list[pos]
        pos_diff, acc_diff = get_state_diff(command, pos, acc)
        next_pos = pos + pos_diff
        if next_pos in pos_seen:
            return acc
        else:
            pos_seen.add(next_pos)
            pos = next_pos
            acc += acc_diff
    return -1

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    command_list = parse_input(file_path)
    answer = calculate_answer(command_list)
    print(answer)