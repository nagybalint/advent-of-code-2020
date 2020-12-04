import os
import re
from typing import Dict

from task1 import parse_passports, count_valid_passports

FIELD_VALIDATORS = {
    "byr": lambda x: digit_comparator(x, 1920, 2002),
    "iyr": lambda x: digit_comparator(x, 2010, 2020),
    "eyr": lambda x: digit_comparator(x, 2020, 2030),
    "hgt": lambda x: height_validator(x),
    "hcl": lambda x: re.compile(r"^#[0-9a-f]{6}$").match(x),
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: re.compile(r"^\d{9}$").match(x) 
}

def digit_comparator(field: str, lower: int, upper: int) -> bool:
    try:
        d = int(field.strip())
        if d >= lower and d <= upper:
            return True
    except:
        return False

def height_validator(field: str) -> bool:
    num = field[:-2]
    measure = field[-2:]
    if measure == 'cm':
        return digit_comparator(num, 150, 193)
    if measure == 'in':
        return digit_comparator(num, 59, 76)
    return False

def is_passport_valid(passport: Dict[str, str]) -> bool:
    for k in FIELD_VALIDATORS:
        if not k in passport:
            return False
        validator = FIELD_VALIDATORS[k]
        if not validator(passport[k]):
            return False
    return True


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    passports = parse_passports(file_path)
    answer = count_valid_passports(passports, is_passport_valid)
    print(f'There are {answer} valid passports')