import os

def parse_input(file_name: str) -> []:
    with open(file_name) as in_file:
        return [line.strip() for line in in_file.readlines()]

def seat_id_to_num(seat_id: str) -> int:
    row = seat_id[:7].replace('F', '0').replace('B', '1')
    col = seat_id[7:].replace('R', '1').replace('L', '0')

    return int(row, 2) * 8 + int(col, 2)

def calculate_answer(in_list):
    return max([seat_id_to_num(e) for e in in_list])


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    in_list = parse_input(file_path)
    answer = calculate_answer(in_list)
    print(answer)