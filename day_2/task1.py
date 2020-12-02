import os
import re
from collections import defaultdict

def parse_input(line: str):
    matcher = re.search(r'(\d*)-(\d*) (.): (.*)', line)
    lower = int(matcher.group(1))
    upper = int(matcher.group(2))
    ch = matcher.group(3)
    password = matcher.group(4)
    return ch, lower, upper, password

def is_password_correct(ch: str, lower: int, upper: int, password: str) -> bool:
    num_of_occurences = password.count(ch)
    if num_of_occurences >= lower and num_of_occurences <= upper:
        return True
    else:
        return False

def get_answer(filepath: str) -> int:
    num_of_correct_passwords = 0
    with open(filepath) as f:
        for line in f.readlines():
            ch, lower, upper, password = parse_input(line)
            if is_password_correct(ch, lower, upper, password):
                num_of_correct_passwords += 1
    return num_of_correct_passwords


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    answer = get_answer(file_path)
    print('There are {answer} correct passwords!')