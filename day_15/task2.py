from task1 import get_number_at_turn

if __name__ == "__main__":
    input_numbers = [9,6,0,10,18,2,1]
    input_turn = 30000000
    answer = get_number_at_turn(input_numbers, input_turn)
    print(answer)