import os
from typing import Tuple, List

class Ship:
    DIRECTION_ORDER = ['E', 'S', 'W', 'N']
    DIRECTION_POS_DELTA = {
        'E': (0, 1),
        'S': (-1, 0),
        'W': (0, -1),
        'N': (1, 0)
    }

    def __init__(self):
        self.pos_north = 0
        self.pos_east = 0
        self.dir = 'E'
    
    def apply_instruction(self, instruction: Tuple[str, int]):
        instr_dir, instr_num = instruction
        if instr_dir in ['L', 'R']:
            self.__execute_turn(instr_dir, instr_num)
            return
        
        if instr_dir in Ship.DIRECTION_POS_DELTA:
            go_to_dir = instr_dir
        elif instr_dir == 'F':
            go_to_dir = self.dir
        else:
            raise Exception('Invalid instruction')

        self.__execute_movement(Ship.DIRECTION_POS_DELTA[go_to_dir], instr_num)
    
    def __execute_movement(self, delta, n):
        delta_n, delta_e = delta
        self.pos_north += (n * delta_n)
        self.pos_east += (n * delta_e)

    def __execute_turn(self, turn_dir, n):
        index_delta = 0
        if turn_dir == 'L':
            index_delta = -1
        elif turn_dir == 'R':
            index_delta = 1
        else:
            raise Exception("Invalid turn instr")

        turn_num = int(n / 90)
        self.dir = Ship.DIRECTION_ORDER[(Ship.DIRECTION_ORDER.index(self.dir) + (index_delta * turn_num)) % 4]

    def get_manhattan_distance(self) -> int:
        return abs(self.pos_north) + abs(self.pos_east)

def parse_input(file_name: str) -> List[Tuple[str, int]]:
    with open(file_name) as in_file:
        return list(map(
            lambda line: (line[0], int(line[1:])), 
            [line.strip() for line in in_file.readlines()]
        ))

def calculate_answer(instructions: List[Tuple[str, int]]) -> int:
    ship = Ship()
    for instr in instructions:
        ship.apply_instruction(instr)
    return ship.get_manhattan_distance()

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    instructions = parse_input(file_path)
    answer = calculate_answer(instructions)
    print(answer)