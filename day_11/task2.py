import os
from typing import List, Tuple
from task1 import parse_input, calculate_answer, Game

def check_in_direction(game_state: List[List[str]], row: int, col: int, direction: Tuple[int, int]) -> int:
    r_dir, c_dir = direction
    row_to_check = row + r_dir
    col_to_check = col + c_dir
    if row_to_check < 0 or row_to_check >= len(game_state):
        return 0
    if col_to_check < 0 or col_to_check >= len(game_state[row_to_check]):
        return 0
    if game_state[row_to_check][col_to_check] == game.TAKEN:
        return 1
    if game_state[row_to_check][col_to_check] == game.EMPTY:
        return 0
    return check_in_direction(game_state, row_to_check, col_to_check, direction)
    
if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    game_map = parse_input(file_path)
    game = Game(check_in_direction, 5)
    answer = calculate_answer(game_map, game)
    print(answer)