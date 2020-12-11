import os
from typing import List

FLOOR = '.'
EMPTY = 'L'
TAKEN = '#'

def parse_input(file_name: str) -> List[List[str]]:
    with open(file_name) as in_file:
        return [list(line.strip()) for line in in_file.readlines()]

def get_number_of_taken_adjacent(game_state: List[List[str]], row: int, col: int) -> int:
    num_of_taken = 0
    for pos in [(-1,-1), (-1, 0), (-1, 1),
                ( 0,-1),          ( 0, 1),
                ( 1,-1), ( 1, 0), ( 1, 1)]:
        try:
            row_to_check = row + pos[0]
            col_to_check = col + pos[1]
            if row_to_check < 0 or col_to_check < 0:
                continue
            elif game_state[row_to_check][col_to_check] == TAKEN:
                num_of_taken += 1
        except:
            continue
    return num_of_taken

def should_be_toggled(game_state: List[List[str]], row: int, col: int) -> bool:
    current_seat = game_state[row][col]
    
    if current_seat == FLOOR:
        return False

    num_of_taken = get_number_of_taken_adjacent(game_state, row, col)
    if current_seat == EMPTY and num_of_taken == 0:
        return True
    if current_seat == TAKEN and num_of_taken >= 4:
        return True
    return False
    

def play_round(game_state: List[List[str]], toggle_rule):
    to_be_toggled = []
    for row in range(len(game_state)):
        for col in range(len(game_state[row])):
            if toggle_rule(game_state, row, col):
                to_be_toggled.append((row, col))
    
    # The hame has ended
    if len(to_be_toggled) == 0:
        return game_state, True
    
    for row, col in to_be_toggled:
        if game_state[row][col] == TAKEN:
            game_state[row][col] = EMPTY
        else:
            game_state[row][col] = TAKEN
    return game_state, False

def play_game(game_state: List[List[str]], toggle_rule) -> List[List[str]]:
    is_game_over = False
    while not is_game_over:
        game_state, is_game_over = play_round(game_state, toggle_rule)
    return game_state

def calculate_answer(game_state: List[List[str]], toggle_rule) -> int:
    final_state = play_game(game_state, toggle_rule)
    num_of_taken = 0
    for row in final_state:
        for seat in row:
            if seat == TAKEN:
                num_of_taken += 1
    return num_of_taken
        

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    game_map = parse_input(file_path)
    answer = calculate_answer(game_map, should_be_toggled)
    print(answer)