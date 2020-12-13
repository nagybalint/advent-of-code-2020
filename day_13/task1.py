import os
from typing import Tuple, List

def parse_input(file_name: str) -> Tuple[int, List[int]]:
    with open(file_name) as f:
        time_of_departure = int(f.readline().strip())
        return time_of_departure, [int(line.strip()) for line in f.readline().strip().split(',') if not line == 'x']

def calculate_answer(time_of_departure: int, bus_ids: List[int]) -> int:
    remaining_minutes = [(bus_id - time_of_departure % bus_id) % bus_id for bus_id in bus_ids]
    minutes_to_wait = min(remaining_minutes)
    bus_to_take = bus_ids[remaining_minutes.index(minutes_to_wait)]
    return minutes_to_wait * bus_to_take

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    time_of_departure, bus_ids = parse_input(file_path)
    answer = calculate_answer(time_of_departure, bus_ids)
    print(answer)