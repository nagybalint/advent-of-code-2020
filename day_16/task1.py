import os
from typing import Callable, Dict, IO, List, Tuple

def parse_input(file_name: str) -> Tuple[Dict[str, Callable[[int], bool]], List[List[int]]]:
    with open(file_name) as f:
        rules = parse_rules(f)
        skip_line(f)
        tickets = parse_tickets(f)
        return rules, tickets

def parse_tickets(f: IO) -> List[List[int]]:
    tickets = []
    line = f.readline().strip()
    tickets.append(parse_ticket(line))
    skip_line(f)
    skip_line(f)
    line = f.readline().strip()
    while line:
        tickets.append(parse_ticket(line))
        line = f.readline().strip()
    return tickets

def parse_rules(f: IO) -> Dict[str, Callable[[int], bool]]:
    rules = {}
    line = f.readline().strip()
    while line:
        name, validator = parse_rule(line)
        rules[name] = validator
        line = f.readline().strip()
    return rules

def skip_line(f: IO):
    f.readline()

def parse_rule(rule: str) -> Tuple[str, Callable[[int], bool]]:
    name, raw_rules = rule.split(": ")
    rule1, rule2 = raw_rules.split(" or ")
    lower1, upper1 = get_rule_limits(rule1)
    lower2, upper2 = get_rule_limits(rule2)
    return name, lambda x: lower1 <= x <= upper1 or lower2 <= x <= upper2

def get_rule_limits(rule: str) -> Tuple[int, int]:
    splits = rule.split("-")
    return int(splits[0]), int(splits[1])

def parse_ticket(ticket: str) -> List[int]:
    return [int(val) for val in ticket.split(',')]

def calculate_answer(rules: Dict[str, Callable[[int], bool]], tickets: List[List[int]]) -> int:
    nearby_tickets = tickets[1:]
    invalid_vals = []
    validators = rules.values()
    for ticket in nearby_tickets:
        for val in ticket:
            validities = [f(val) for f in validators]
            if not any(validities):
                invalid_vals.append(val)
    return sum(invalid_vals)

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')
    rules, tickets = parse_input(file_path)
    answer = calculate_answer(rules, tickets)
    print(answer)