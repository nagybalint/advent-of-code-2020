import os
from typing import List, Tuple
from task1 import FLOOR, EMPTY, TAKEN, parse_input, calculate_answer

def get_number_of_taken_adjacent(game_state: List[List[str]], row: int, col: int) -> int:
    num_of_taken = 0
    for pos in [(-1,-1), (-1, 0), (-1, 1),
                ( 0,-1),          ( 0, 1),
                ( 1,-1), ( 1, 0), ( 1, 1)]:
        num_of_taken += check_in_direction(game_state, row, col, pos)
    return num_of_taken

def check_in_direction(game_state: List[List[str]], row: int, col: int, direction: Tuple[int, int]) -> int:
    r_dir, c_dir = direction
    row_to_check = row + r_dir
    col_to_check = col + c_dir
    if row_to_check < 0 or row_to_check >= len(game_state):
        return 0
    if col_to_check < 0 or col_to_check >= len(game_state[row_to_check]):
        return 0
    if game_state[row_to_check][col_to_check] == TAKEN:
        return 1
    if game_state[row_to_check][col_to_check] == EMPTY:
        return 0
    return check_in_direction(game_state, row_to_check, col_to_check, direction)


def should_be_toggled(game_state: List[List[str]], row: int, col: int) -> bool:
    current_seat = game_state[row][col]
    
    if current_seat == FLOOR:
        return False

    num_of_taken = get_number_of_taken_adjacent(game_state, row, col)
    if current_seat == EMPTY and num_of_taken == 0:
        return True
    if current_seat == TAKEN and num_of_taken >= 5:
        return True
    return False
    
if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    game_map = parse_input(file_path)
    answer = calculate_answer(game_map, should_be_toggled)
    print(answer)