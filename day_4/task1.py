import os
from typing import Dict, List

PASSPORT_FIELD = ["byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid"]

def parse_passports(file_path: str) -> List[Dict[str, str]]:
    passports = []
    with open(file_path) as f:
        passport_details = []
        for line in f.readlines():
            passport_line = line.strip()
            if passport_line == "":
                passports.extend([passport_from_details(" ".join(passport_details))])
                passport_details = []
            else:
                passport_details.extend([passport_line])
    return passports

def passport_from_details(passport_details: str) -> Dict[str, str]:
    passport = {}
    for detail in passport_details.split(" "):
        detail = detail.strip()
        if detail != "":
            k, v = detail.split(":")
            passport[k] = v
    return passport

def is_passport_valid(passport: Dict[str, str]) -> bool:
    for k in PASSPORT_FIELD[:-1]:
        if not k in passport:
            return False
    return True

def count_valid_passports(passports: List[Dict[str, str]], validator) -> int:
    num_of_valid_passports = 0
    for passport in passports:
        if validator(passport):
            num_of_valid_passports += 1
    return num_of_valid_passports

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    passports = parse_passports(file_path)
    answer = count_valid_passports(passports, is_passport_valid)
    print(f'There are {answer} valid passports')
    