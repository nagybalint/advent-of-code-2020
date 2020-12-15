from typing import List

def get_number_at_turn(input_numbers: List[int], max_turn: int) -> int:
    number_age_dict = {num: i + 1 for i, num in enumerate(input_numbers)}
    current_turn = len(input_numbers) + 1
    next_number = current_turn - number_age_dict[input_numbers[-1]] - 1

    while current_turn <= max_turn:
        number_spoken = next_number
        try:
            next_number = current_turn - number_age_dict[number_spoken]
        except:
            next_number = 0
        number_age_dict[number_spoken] = current_turn
        current_turn += 1

    return number_spoken

if __name__ == "__main__":
    input_numbers = [9,6,0,10,18,2,1]
    input_turn = 2020
    answer = get_number_at_turn(input_numbers, input_turn)
    print(answer)