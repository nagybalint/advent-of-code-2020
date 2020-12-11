import os
from typing import List, Tuple

class Game:
    FLOOR = '.'
    EMPTY = 'L'
    TAKEN = '#'

    def __init__(self, check_fun, leave_seat_tolerance):
        self.check_fun = check_fun
        self.leave_seat_tolerance = leave_seat_tolerance

def parse_input(file_name: str) -> List[List[str]]:
    with open(file_name) as in_file:
        return [list(line.strip()) for line in in_file.readlines()]

def get_number_of_taken_adjacent(game_state: List[List[str]], row: int, col: int, check_fun) -> int:
    num_of_taken = 0
    for pos in [(-1,-1), (-1, 0), (-1, 1),
                ( 0,-1),          ( 0, 1),
                ( 1,-1), ( 1, 0), ( 1, 1)]:
        num_of_taken += check_fun(game_state, row, col, pos)
    return num_of_taken

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
    return 0

def should_be_toggled(game_state: List[List[str]], row: int, col: int, game) -> bool:
    current_seat = game_state[row][col]
    
    if current_seat == game.FLOOR:
        return False

    num_of_taken = get_number_of_taken_adjacent(game_state, row, col, game.check_fun)
    if current_seat == game.EMPTY and num_of_taken == 0:
        return True
    if current_seat == game.TAKEN and num_of_taken >= game.leave_seat_tolerance:
        return True
    return False
    

def play_round(game_state: List[List[str]], game):
    to_be_toggled = []
    for row in range(len(game_state)):
        for col in range(len(game_state[row])):
            if should_be_toggled(game_state, row, col, game):
                to_be_toggled.append((row, col))
    
    # The hame has ended
    if len(to_be_toggled) == 0:
        return game_state, True
    
    for row, col in to_be_toggled:
        if game_state[row][col] == game.TAKEN:
            game_state[row][col] = game.EMPTY
        else:
            game_state[row][col] = game.TAKEN
    return game_state, False

def play_game(game_state: List[List[str]], game) -> List[List[str]]:
    is_game_over = False
    while not is_game_over:
        game_state, is_game_over = play_round(game_state, game)
    return game_state

def calculate_answer(game_state: List[List[str]], game) -> int:
    final_state = play_game(game_state, game)
    num_of_taken = 0
    for row in final_state:
        for seat in row:
            if seat == game.TAKEN:
                num_of_taken += 1
    return num_of_taken
        

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    game_map = parse_input(file_path)
    game = Game(check_in_direction, 4)
    answer = calculate_answer(game_map, game)
    print(answer)