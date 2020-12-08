import os
from typing import List, Tuple
from task1 import get_state_diff, parse_input, parse_command

def toggle_nop_jmp(command: str) -> str:
    cmd_type, num = parse_command(command)
    if cmd_type == "jmp":
        return "nop +0"
    elif cmd_type == "nop":
        return f"jmp {command[4:]}"
    else:
        raise Exception("Invalid toggle")

def calculate_answer(command_list: List[str]) -> int:
    for game in generate_games(command_list):
        try:
            acc = play_game(game)
            return acc
        except:
            pass
    else:
        return -1

def generate_games(command_list: List[str]):
    for i in range(len(command_list)):
        original_command = command_list[i]
        cmd_type, num = parse_command(original_command)
        if cmd_type == "acc":
            continue
        command_list[i] = toggle_nop_jmp(original_command)
        yield command_list
        command_list[i] = original_command

def play_game(command_list: List[str]) -> int:
    pos = acc = 0
    pos_seen = set([0])
    while pos < len(command_list):
        command = command_list[pos]
        pos_diff, acc_diff = get_state_diff(command, pos, acc)
        next_pos = pos + pos_diff
        if next_pos in pos_seen:
            raise Exception()
        else:
            pos_seen.add(next_pos)
            pos = next_pos
            acc += acc_diff
    return acc

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    command_list = parse_input(file_path)
    answer = calculate_answer(command_list)
    print(answer)