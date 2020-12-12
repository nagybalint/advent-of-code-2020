import os
from typing import Tuple
from task1 import parse_input, calculate_answer, Ship

class WaypointShip(Ship):
    def __init__(self):
        super().__init__()
        self.waypoint_north = 1
        self.waypoint_east = 10
    
    def apply_instruction(self, instruction: Tuple[str, int]):
        instr_dir, instr_num = instruction
        if instr_dir in ['L', 'R']:
            self.__turn_waypoint(instr_dir, instr_num)
            return
        elif instr_dir == 'F':
            self._execute_movement((self.waypoint_north, self.waypoint_east), instr_num)
        else:
            delta = WaypointShip.DIRECTION_POS_DELTA[instr_dir]
            self.__move_waypoint(delta, instr_num)

    def __move_waypoint(self, delta, n):
        delta_n, delta_e = delta
        self.waypoint_north += (n * delta_n)
        self.waypoint_east += (n * delta_e)

    @staticmethod
    def turn_point_90_degress_around_origin(pos_n, pos_e, turn_dir):
        new_pos_n = pos_e
        new_pos_e = pos_n
        if turn_dir == 'L':
            new_pos_e *= -1
        else:
            new_pos_n *= -1
        return new_pos_n, new_pos_e
        
    def __turn_waypoint(self, turn_dir, n):                
        turns_to_do = int(n / 90)
        pos_n = self.waypoint_north
        pos_e = self.waypoint_east
        for _ in range(turns_to_do):
            pos_n, pos_e = self.turn_point_90_degress_around_origin(pos_n, pos_e, turn_dir)
        self.waypoint_north = pos_n
        self.waypoint_east = pos_e

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    instructions = parse_input(file_path)
    answer = calculate_answer(instructions, WaypointShip())
    print(answer)