import os
from task1 import seat_id_to_num, parse_input

def get_set_num(in_list):
    seats = [seat_id_to_num(seat) for seat in in_list]
    seats.sort()
    for i in range(1, len(seats)):
        if seats[i] - seats[i - 1] == 2:
            return seats[i] - 1
    raise Exception()

def calculate_answer(in_list):
    return get_set_num(in_list)

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    in_list = parse_input(file_path)
    answer = calculate_answer(in_list)
    print(answer)