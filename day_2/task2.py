import os
import re
from task1 import get_answer

def is_password_correct(ch: str, lower: int, upper: int, password: str) -> bool:
    pw_chars = list(password)
    a = None
    b = None
    if lower <= len(pw_chars):
        a = pw_chars[lower - 1]
    if upper <= len(pw_chars):
        b = pw_chars[upper - 1]
    if a == b: 
        return False
    if a == ch or b == ch:
        return True
    return False

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    answer = get_answer(file_path, is_password_correct)
    print('There are {answer} correct passwords!')